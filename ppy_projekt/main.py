import sqlite3
import tkinter as tk

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandastable import Table
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

model = None
x_train, x_test, y_train, y_test = 0, 0, 0, 0
database_connection = None


def train():
    global model, database_connection
    database_connection = sqlite3.connect("baza.db")
    if model is not None:
        info_label.config(text="Model jest już wytrenowany")
    else:
        model = KNeighborsClassifier(n_neighbors=5)

        headers = ["TypeOf", "Alcohol", "Malic_acid", "Ash", "Alcalinity_of_ash", "Magnesium", "Total_phenols",
                   "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue",
                   "OD280_OD315_of_diluted_wines", "Proline"]
        # df = pd.read_csv("wine.data", names=headers)
        df = pd.read_sql_query("SELECT * FROM wines", database_connection)

        x = df.iloc[:, 1:]
        y = df.iloc[:, 0]

        global x_train, x_test, y_train, y_test
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=2137)
        model.fit(x_train, y_train)
        info_label.config(text="Poprawnie wytrenowano model")


def test():
    global model, x_train, y_train
    if model is None:
        info_label.config(text="Model nie jest wytrenowany")
    else:
        global x_test, y_test

        kfold = KFold(n_splits=5, random_state=2023, shuffle=True)
        scores = cross_val_score(model, x_train, y_train, cv=kfold, scoring="accuracy")
        info_label.config(text=f"Wyniki testu:\n {scores}\nŚrednia dokładność: {scores.mean()}")


def predict():
    try:
        global model
        global x_train
        if model is None:
            info_label.config(text="Model nie jest wytrenowany")
        else:
            dane = enter.get()
            dane = dane.split(sep=",")
            new_df = pd.DataFrame([dane], columns=x_train.columns)
            predicition = model.predict(new_df)
            info_label.config(text=f"Dla danych {enter.get()}\nprzewidywana klasa to: {predicition}")
    except:
        info_label.config(text="Podano nieprawidłowy format danych")


def add():
    try:
        global model, x_train, y_train, database_connection
        dane = add_field.get()
        dane = dane.split(sep=",")
        new_df = pd.DataFrame([dane], columns=x_train.columns)
        df = pd.read_sql_query("SELECT * FROM wines", database_connection)
        pd.concat([df, new_df])
        info_label.config(text=f"Dodano dane {add_field.get()} do bazy")
        df.to_sql("wines", database_connection, if_exists="replace", index=False)
    except:
        info_label.config(text="Podano nieprawidłowy format danych")


def retrain():
    global model, x_train, x_test, y_train, y_test
    if model is None:
        info_label.config(text="Najpierw wytrenuj model")
    else:
        df = pd.read_sql_query("SELECT * FROM wines", database_connection)

        x = df.iloc[:, 1:]
        y = df.iloc[:, 0]

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=137)
        model.fit(x_train, y_train)
        info_label.config(text="Wytrenowano model ponownie")


def table():
    global database_connection, model
    if model is None:
        train()
    table_window = tk.Toplevel(root)
    table_window.title("Tabela")
    table_window.geometry("600x400")

    data = pd.read_sql_query("SELECT * FROM wines", database_connection)

    frame = tk.Frame(table_window)
    frame.pack()

    pt = Table(frame)
    pt.show()
    pt.model.df = data


def graph():
    global database_connection, model
    if model is None:
        train()

    graph_window = tk.Toplevel(root)
    graph_window.title("Wykres")
    graph_window.geometry("1600x1400")
    frame_graph = tk.Frame(graph_window, borderwidth=4, relief="ridge")
    frame_graph.pack(padx=10, pady=10)

    df1 = pd.read_sql_query("SELECT * FROM wines WHERE TypeOf = 1", database_connection)
    df2 = pd.read_sql_query("SELECT * FROM wines WHERE TypeOf = 2", database_connection)
    df3 = pd.read_sql_query("SELECT * FROM wines WHERE TypeOf = 3", database_connection)

    figure1 = plt.Figure(figsize=(4, 3), dpi=100)
    ax = figure1.add_subplot(111)
    bar = FigureCanvasTkAgg(figure1, frame_graph)
    bar.get_tk_widget().pack()
    df1.plot(kind="line", legend=False, ax=ax)
    ax.set_title("Type 1")

    figure2 = plt.Figure(figsize=(4, 3), dpi=100)
    ax = figure2.add_subplot(111)
    bar = FigureCanvasTkAgg(figure2, frame_graph)
    bar.get_tk_widget().pack()
    df2.plot(kind="line", legend=False, ax=ax)
    ax.set_title("Type 2")

    figure3 = plt.Figure(figsize=(4, 3), dpi=100)
    ax = figure3.add_subplot(111)
    bar = FigureCanvasTkAgg(figure3, frame_graph)
    bar.get_tk_widget().pack()
    df3.plot(kind="line", legend=False, ax=ax)
    ax.set_title("Type 3")


root = tk.Tk()

root.title("Wine Classifier")
root.geometry("800x600")


info_frame = tk.Frame(root, borderwidth=4, relief="ridge")
info_frame.pack(padx=10, pady=10)
info_label = tk.Label(info_frame, text="Tutaj pojawią się informacje")
info_label.pack()

frame = tk.Frame(root, borderwidth=4, relief="ridge")
frame.pack(padx=10, pady=10)
button = tk.Button(frame, text="Trenuj model", command=train)
button.pack()

frame = tk.Frame(root, borderwidth=4, relief="ridge")
frame.pack(padx=10, pady=10)
button = tk.Button(frame, text="Testuj model", command=test)
button.pack()

frame = tk.Frame(root, borderwidth=4, relief="ridge")
frame.pack(padx=10, pady=10)
enter = tk.Entry(frame)
enter.pack()
button = tk.Button(frame, text="Klasyfikuj dane", command=predict)
button.pack()

frame = tk.Frame(root, borderwidth=4, relief="ridge")
frame.pack(padx=10, pady=10)
add_field = tk.Entry(frame)
add_field.pack()
button = tk.Button(frame, text="Dodaj dane", command=add)
button.pack()

frame = tk.Frame(root, borderwidth=4, relief="ridge")
frame.pack(padx=10, pady=10)
button = tk.Button(frame, text="Trenuj ponownie", command=retrain)
button.pack()

frame = tk.Frame(root, borderwidth=4, relief="ridge")
frame.pack(padx=10, pady=10)
button = tk.Button(frame, text="Pokaż table danych", command=table)
button.pack()

frame = tk.Frame(root, borderwidth=4, relief="ridge")
frame.pack(padx=10, pady=10)
button = tk.Button(frame, text="Pokaż wykres", command=graph)
button.pack()

root.mainloop()
