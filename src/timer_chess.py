import tkinter as tk

# An app
class App():

    def __init__(self):
        
        # parameters
        self.minute = 40
        self.second = 0
        self.minute_player1 = 20
        self.minute_player2 = 20
        self.seconde_player1 = 0
        self.seconde_player2 = 0
        self.time = self.minute,":", self.second
        self.time_player1 = self.minute_player1,":", self.seconde_player1
        self.time_player2 = self.minute_player2,":", self.seconde_player2
        self.who = True # true when player1 is playing
        self.text_button1 = "start"
        self.text_button2 = "start"

        # screen
        self.app = tk.Tk()
        self.app.geometry("300x150")
        self.app.title("Chess timer")
        self.init_widget()

    # if the button1 is selected
    def loop_time1(self):

        if self.button1["text"] == "start":
            self.button1["text"] = "stop"
            self.button2["text"] = "stop"
            self.button2["state"] = tk.DISABLED
            self.button2["bg"] = "red"
            self.button2["fg"] = "white"

            # it allows us to update the players' times
            self.app.after(1000, self.time_increment) 

        elif self.button1["text"] == "stop":
            self.button1["state"] = tk.DISABLED
            self.button1["bg"] = "red"
            self.button2["fg"] = "white"
            self.button2["state"] = tk.NORMAL
            self.button2["bg"] = "green"
            self.button2["fg"] = "black"

    # if the button2 is selected
    def loop_time2(self):

        if self.button2["text"] == "start":
            self.button1["text"] = "stop"
            self.button2["text"] = "stop"
            self.button2["state"] = tk.DISABLED
            self.button2["bg"] = "red"
            self.button2["fg"] = "white"

            # it allows us to update the players' times
            self.app.after(1000, self.time_increment) 

        elif self.button2["text"] == "stop":
            self.button1["state"] = tk.NORMAL
            self.button1["bg"] = "green"
            self.button1["fg"] = "black"
            self.button2["state"] = tk.DISABLED
            self.button2["bg"] = "red"
            self.button2["fg"] = "white"

    def time_increment(self):

        if self.second == 0 and self.minute != 0:
            self.minute -= 1
            self.second = 60

        if self.minute == 0 and self.second == 0:
            print("It's finished !")
            time = self.minute,":", self.second
            self.text1["text"] = time,"\nIt's finished"

        else:
            
            if self.button1["state"] == tk.DISABLED:
                self.seconde_player1, self.minute_player1 = self.time_increment_player(self.minute_player1, self.seconde_player1, self.text3)

            else:
                self.seconde_player2, self.minute_player2 = self.time_increment_player(self.minute_player2, self.seconde_player2, self.text2)

            self.second -= 1
            time = self.minute,":", self.second
            self.text1["text"] = time
            self.app.after(1000, self.time_increment)

    def time_increment_player(self, minute, second, text):
        if second == 0 and minute != 0:
            minute -= 1
            second = 60

        if minute == 0 and second == 0:
            print("It's finished !")
            time = minute,":",second
            text["text"] = time,"\nIt's finished"

        else:
            second -= 1
            time = minute,":",second
            text["text"] = time
            return second, minute

    def init_widget(self):
        # widgets
        self.canvas = tk.Canvas(self.app)
        self.canvas.grid(row=2, column=2)

        self.text1 = tk.Label(text=self.time)
        self.text1.place(relx=0.5, rely=0, anchor=tk.N)

        self.text2 = tk.Label(self.canvas, text=self.time_player1)
        self.text2.place(relx=0.2, rely=0.2, anchor=tk.W)

        self.text3 = tk.Label(self.canvas, text=self.time_player2)
        self.text3.place(relx=0.6, rely=0.2, anchor=tk.E)

        self.button1 = tk.Button(self.canvas, text=self.text_button1, command=self.loop_time1, bg="green")
        self.button1.place(relx=0.2, rely=0.4, anchor=tk.SW)

        self.button2 = tk.Button(self.canvas, text=self.text_button2, command=self.loop_time2, bg="green")
        self.button2.place(relx=0.6, rely=0.4, anchor=tk.SE)

if __name__ == '__main__':
    app = App()
    app.app.mainloop()