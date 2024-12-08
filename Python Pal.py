import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import sys
import os
import json

class ProgramPracticeApp:
    SETTINGS_FILE = 'settings.json'
    USER_CREDENTIALS_FILE = 'users.json'
    
    def __init__(self, root):
        self.root = root
        self.root.title("Python Pal")
        self.root.geometry("1600x800")  # Adjusted window size for better display
        self.timeout = 5
        self.dark_mode = False
        self.load_settings()

        self.programs = {
            "App Development": [
                ("Basic Calculator", """import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = str(eval(entry.get()))  # Evaluate the expression entered
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, result)  # Display the result
    except Exception as e:
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, "Error")  # Show error message if invalid input

# Function to update the entry field
def button_click(value):
    current = entry.get()  # Get current text in the entry field
    entry.delete(0, tk.END)  # Clear the entry field
    entry.insert(tk.END, current + value)  # Add new value to the field

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("Basic Calculator")

# Create entry widget for displaying input and result
entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout and creation
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create buttons and place them in the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=evaluate_expression)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = tk.Button(window, text="C", width=5, height=2, font=("Arial", 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the GUI loop
window.mainloop()
 """),
                ("To-Do List", """import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)  # Clear the input field after adding task
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a selected task from the list
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()  # Get the index of selected task
        task_listbox.delete(selected_task_index)  # Remove the selected task
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to clear all tasks from the list
def clear_all_tasks():
    task_listbox.delete(0, tk.END)  # Clear all tasks in the list

# Create main window
window = tk.Tk()
window.title("To-Do List")

# Create entry widget for task input
task_entry = tk.Entry(window, width=30, font=("Arial", 14))
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Create add task button
add_button = tk.Button(window, text="Add Task", width=15, height=2, font=("Arial", 14), command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Create delete task button
delete_button = tk.Button(window, text="Delete Task", width=15, height=2, font=("Arial", 14), command=delete_task)
delete_button.grid(row=1, column=1, padx=10, pady=10)

# Create clear all tasks button
clear_button = tk.Button(window, text="Clear All", width=15, height=2, font=("Arial", 14), command=clear_all_tasks)
clear_button.grid(row=2, column=1, padx=10, pady=10)

# Create listbox to display tasks
task_listbox = tk.Listbox(window, width=50, height=10, font=("Arial", 14))
task_listbox.grid(row=1, column=0, rowspan=2, padx=10, pady=10)

# Run the GUI loop
window.mainloop()
"""),
                ("Unit Converter", """import tkinter as tk
from tkinter import messagebox

# Function to convert kilometers to miles
def km_to_miles():
    try:
        km = float(entry.get())
        miles = km * 0.621371
        result_label.config(text=f"{km} kilometers = {miles:.2f} miles")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number.")

# Function to convert miles to kilometers
def miles_to_km():
    try:
        miles = float(entry.get())
        km = miles / 0.621371
        result_label.config(text=f"{miles} miles = {km:.2f} kilometers")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number.")

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number.")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit} Fahrenheit = {celsius:.2f} Celsius")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number.")

# Create main window
window = tk.Tk()
window.title("Unit Converter")

# Create entry widget for input
entry_label = tk.Label(window, text="Enter value:", font=("Arial", 14))
entry_label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(window, width=20, font=("Arial", 14))
entry.grid(row=0, column=1, padx=10, pady=10)

# Create conversion buttons
km_miles_button = tk.Button(window, text="Km to Miles", font=("Arial", 14), command=km_to_miles)
km_miles_button.grid(row=1, column=0, padx=10, pady=10)

miles_km_button = tk.Button(window, text="Miles to Km", font=("Arial", 14), command=miles_to_km)
miles_km_button.grid(row=1, column=1, padx=10, pady=10)

celsius_fahrenheit_button = tk.Button(window, text="Celsius to Fahrenheit", font=("Arial", 14), command=celsius_to_fahrenheit)
celsius_fahrenheit_button.grid(row=2, column=0, padx=10, pady=10)

fahrenheit_celsius_button = tk.Button(window, text="Fahrenheit to Celsius", font=("Arial", 14), command=fahrenheit_to_celsius)
fahrenheit_celsius_button.grid(row=2, column=1, padx=10, pady=10)

# Create label to display result
result_label = tk.Label(window, text="Result will be displayed here", font=("Arial", 14), width=30)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI loop
window.mainloop()
"""),
                ("Weather App", """import tkinter as tk
import requests
from tkinter import messagebox

# Function to get weather information
def get_weather():
    city = city_entry.get()
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Fetch weather data
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            result_label.config(text=f"Weather: {weather_description}\nTemperature: {temperature}°C\n"
                                    f"Humidity: {humidity}%\nWind Speed: {wind_speed} m/s")
        else:
            messagebox.showerror("Error", "City not found or invalid.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create labels, entry, and button
city_label = tk.Label(window, text="Enter City Name:", font=("Arial", 14))
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(window, font=("Arial", 14))
city_entry.grid(row=0, column=1, padx=10, pady=10)

get_weather_button = tk.Button(window, text="Get Weather", font=("Arial", 14), command=get_weather)
get_weather_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Result label to display weather info
result_label = tk.Label(window, text="Weather data will be shown here.", font=("Arial", 14), width=50, height=10, justify="left")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI loop
window.mainloop()
"""),
                ("Quiz Game", """import tkinter as tk
from tkinter import messagebox

# List of questions, options, and correct answers
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Hemingway", "Fitzgerald"], "answer": "Shakespeare"},
    {"question": "What is the largest animal on Earth?", "options": ["Elephant", "Blue Whale", "Shark", "Giraffe"], "answer": "Blue Whale"}
]

current_question = 0  # Keeps track of the current question index
score = 0  # User's score

# Function to show the next question
def show_next_question():
    global current_question
    if current_question < len(questions):
        question = questions[current_question]
        question_label.config(text=question["question"])
        for i in range(4):
            option_buttons[i].config(text=question["options"][i])
    else:
        messagebox.showinfo("Quiz Over", f"Your score: {score}/{len(questions)}")
        window.quit()

# Function to check the answer
def check_answer(selected_option):
    global current_question, score
    if questions[current_question]["options"][selected_option] == questions[current_question]["answer"]:
        score += 1
    current_question += 1
    show_next_question()

# Create the main window
window = tk.Tk()
window.title("Quiz Game")

# Create label for displaying question
question_label = tk.Label(window, text="", font=("Arial", 16), width=50, height=3, anchor="w")
question_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for options
option_buttons = []
for i in range(4):
    button = tk.Button(window, text="", font=("Arial", 14), width=30, height=2, command=lambda i=i: check_answer(i))
    button.grid(row=i+1, column=0, columnspan=4, padx=10, pady=5)
    option_buttons.append(button)

# Start the quiz
show_next_question()

# Run the GUI loop
window.mainloop()
"""),
                ("Password Generator", """import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())  # Get the password length from the input field
    if length < 4:
        messagebox.showwarning("Input Error", "Password length should be at least 4 characters.")
        return

    # Create a pool of characters (letters, digits, and special characters)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))

    # Display the generated password in the result label
    password_label.config(text=f"Generated Password: {password}")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create input label for password length
length_label = tk.Label(window, text="Enter password length:", font=("Arial", 14))
length_label.grid(row=0, column=0, padx=10, pady=10)

# Create entry widget to input the password length
length_entry = tk.Entry(window, font=("Arial", 14))
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Create button to generate the password
generate_button = tk.Button(window, text="Generate Password", font=("Arial", 14), command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create label to display the generated password
password_label = tk.Label(window, text="Generated Password will appear here.", font=("Arial", 14), width=50, height=3, anchor="w")
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI loop
window.mainloop()
"""),
                ("BMI Calculator", """import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())  # Get weight from the input field
        height = float(height_entry.get())  # Get height from the input field
        
        if weight <= 0 or height <= 0:
            messagebox.showwarning("Input Error", "Weight and height must be positive values.")
            return

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        # Display BMI result
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter valid numerical values for weight and height.")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create labels and entry widgets for weight and height
weight_label = tk.Label(window, text="Enter weight (kg):", font=("Arial", 14))
weight_label.grid(row=0, column=0, padx=10, pady=10)

weight_entry = tk.Entry(window, font=("Arial", 14))
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(window, text="Enter height (m):", font=("Arial", 14))
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = tk.Entry(window, font=("Arial", 14))
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Create button to calculate BMI
calculate_button = tk.Button(window, text="Calculate BMI", font=("Arial", 14), command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create label to display the result
result_label = tk.Label(window, text="BMI result will be displayed here.", font=("Arial", 14), width=40, height=4, anchor="w")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI loop
window.mainloop()
"""),
                ("Timer/Stopwatch", """import tkinter as tk
import time

# Timer class to handle time-related operations
class TimerStopwatch:
    def __init__(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.update_time = 0

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_time_display()

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.elapsed_time = 0
        if self.running:
            self.start_time = time.time()
        self.update_time_display()

    def update_time_display(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.window.after(100, self.update_time_display)

        seconds = int(self.elapsed_time)
        minutes = seconds // 60
        seconds = seconds % 60
        hours = minutes // 60
        minutes = minutes % 60

        # Format the time in HH:MM:SS format
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        time_label.config(text=time_str)

    def set_window(self, window, time_label):
        self.window = window
        self.time_label = time_label

# Create the main window
window = tk.Tk()
window.title("Timer/Stopwatch")

# Create a TimerStopwatch instance
timer_stopwatch = TimerStopwatch()

# Create label to display time
time_label = tk.Label(window, text="00:00:00", font=("Arial", 40), width=10, height=2)
time_label.grid(row=0, column=0, padx=10, pady=10)

# Set window and time_label in the TimerStopwatch instance
timer_stopwatch.set_window(window, time_label)

# Create start, stop, and reset buttons
start_button = tk.Button(window, text="Start", font=("Arial", 14), width=10, height=2, command=timer_stopwatch.start)
start_button.grid(row=1, column=0, padx=10, pady=5)

stop_button = tk.Button(window, text="Stop", font=("Arial", 14), width=10, height=2, command=timer_stopwatch.stop)
stop_button.grid(row=1, column=1, padx=10, pady=5)

reset_button = tk.Button(window, text="Reset", font=("Arial", 14), width=10, height=2, command=timer_stopwatch.reset)
reset_button.grid(row=1, column=2, padx=10, pady=5)

# Run the GUI loop
window.mainloop()
""")
            ],
        "Game Development": [("2D Mario-Style Game", """
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Mario-Style Game")
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)

# Player settings
player = {
    "x": WIDTH // 2,
    "y": HEIGHT - 50,
    "width": 40,
    "height": 40,
    "speed": 5,
    "jump_power": 15,
    "gravity": 1,
    "velocity_y": 0,
    "is_jumping": False
}

# Platform settings
platforms = [
    {
        "x": random.randint(50, WIDTH - 150),
        "y": random.randint(200, HEIGHT - 50),
        "width": random.randint(100, 200),
        "height": 20,
    }
    for _ in range(10)
]

# Function to draw rectangles
def draw_rect(x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))

# Game loop
def main():
    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player["x"] > 0:
            player["x"] -= player["speed"]
        if keys[pygame.K_RIGHT] and player["x"] < WIDTH - player["width"]:
            player["x"] += player["speed"]
        if not player["is_jumping"] and keys[pygame.K_SPACE]:
            player["is_jumping"] = True
            player["velocity_y"] = -player["jump_power"]

        # Apply gravity
        if player["is_jumping"]:
            player["velocity_y"] += player["gravity"]
            player["y"] += player["velocity_y"]

        # Check collision with platforms
        for platform in platforms:
            if (platform["x"] <= player["x"] <= platform["x"] + platform["width"]
                    and platform["y"] <= player["y"] + player["height"] <= platform["y"] + platform["height"]
                    and player["velocity_y"] > 0):
                player["y"] = platform["y"] - player["height"]
                player["velocity_y"] = 0
                player["is_jumping"] = False

        # Draw platforms
        for platform in platforms:
            draw_rect(platform["x"], platform["y"], platform["width"], platform["height"], BROWN)

        # Draw player
        draw_rect(player["x"], player["y"], player["width"], player["height"], BLUE)

        # Update screen
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
""")

               
,
("Tic-Tac-Toe Game", """import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Game variables
turn = "X"
board = [""] * 9  # To track the moves (empty initially)

# Function to handle button click
def button_click(index):
    global turn

    # If the clicked cell is empty, proceed with the move
    if board[index] == "":
        board[index] = turn
        buttons[index].config(text=turn)
        
        # Check for a winner
        if check_winner(turn):
            messagebox.showinfo("Game Over", f"Player {turn} wins!")
            reset_game()
            return
        
        # Check for a draw
        if "" not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
            return

        # Switch turns
        turn = "O" if turn == "X" else "X"

# Function to check if there is a winner
def check_winner(player):
    # Winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to reset the game
def reset_game():
    global turn, board
    turn = "X"
    board = [""] * 9
    for button in buttons:
        button.config(text="")

# Create buttons for the Tic-Tac-Toe grid
buttons = []
for i in range(9):
    button = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), 
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the main event loop
root.mainloop()
"""),
("Snake Game", """import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up display
width = 600
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set up the clock
clock = pygame.time.Clock()

# Set up snake and food parameters
snake_block = 10
snake_speed = 15

# Set up font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    window.blit(value, [0, 0])

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

# Function to display the message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

# Main function to handle the game
def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = width / 2
    y1 = height / 2

    # Snake movement
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Game loop
    while not game_over:

        while game_close:
            window.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # Check for user input after losing
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Handle key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Game boundaries logic
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(blue)

        pygame.draw.rect(window, yellow, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check for collision with food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Control the game speed
        clock.tick(snake_speed)

    # Quit the game
    pygame.quit()
    quit()

# Run the game loop
gameLoop()
"""),
("Car Racing Game", """import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Load assets
car_width = 50
car_height = 100
player_car = pygame.Surface((car_width, car_height))
player_car.fill(BLUE)

# Enemy cars
enemy_width = 50
enemy_height = 100
enemy_color = RED

# Functions
def draw_text(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))

def main_game():
    running = True
    font = pygame.font.SysFont(None, 40)

    # Player car position
    player_x = WIDTH // 2 - car_width // 2
    player_y = HEIGHT - car_height - 20

    # Enemy car details
    enemy_x = random.randint(0, WIDTH - enemy_width)
    enemy_y = -enemy_height
    enemy_speed = 5

    # Score
    score = 0

    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the player's car
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= 7
        if keys[pygame.K_RIGHT] and player_x < WIDTH - car_width:
            player_x += 7

        # Enemy car movement
        enemy_y += enemy_speed
        if enemy_y > HEIGHT:
            enemy_y = -enemy_height
            enemy_x = random.randint(0, WIDTH - enemy_width)
            score += 1  # Increase score

        # Check for collisions
        if (player_x < enemy_x + enemy_width and
            player_x + car_width > enemy_x and
            player_y < enemy_y + enemy_height and
            player_y + car_height > enemy_y):
            draw_text("GAME OVER", font, RED, WIDTH // 2 - 100, HEIGHT // 2)
            pygame.display.update()
            pygame.time.wait(2000)
            running = False

        # Drawing the player car
        screen.blit(player_car, (player_x, player_y))

        # Drawing the enemy car
        pygame.draw.rect(screen, enemy_color, (enemy_x, enemy_y, enemy_width, enemy_height))

        # Display the score
        draw_text(f"Score: {score}", font, BLACK, 10, 10)

        # Update the display
        pygame.display.update()
        clock.tick(FPS)

# Start the game
main_game()
pygame.quit()

"""),
("Shooter Game", """import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player properties
player_width = 50
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 7

# Bullet properties
bullet_width = 5
bullet_height = 10
bullet_speed = -10
bullets = []

# Enemy properties
enemy_width = 50
enemy_height = 30
enemies = []
enemy_speed = 3
spawn_delay = 30
spawn_timer = 0

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Functions
def draw_text(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))

def spawn_enemy():
    x = random.randint(0, WIDTH - enemy_width)
    y = random.randint(-100, -40)
    enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))

def main_game():
    global spawn_timer, score

    running = True
    player = pygame.Rect(player_x, player_y, player_width, player_height)

    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x < WIDTH - player_width:
            player.x += player_speed
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:  # Limit bullets on screen
                bullets.append(pygame.Rect(player.centerx - bullet_width // 2, player.y, bullet_width, bullet_height))

        # Update bullets
        for bullet in bullets[:]:
            bullet.y += bullet_speed
            if bullet.y < 0:
                bullets.remove(bullet)

        # Spawn enemies
        spawn_timer += 1
        if spawn_timer >= spawn_delay:
            spawn_enemy()
            spawn_timer = 0

        # Update enemies
        for enemy in enemies[:]:
            enemy.y += enemy_speed
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
            if player.colliderect(enemy):
                draw_text("GAME OVER", font, RED, WIDTH // 2 - 100, HEIGHT // 2)
                pygame.display.update()
                pygame.time.wait(2000)
                running = False

        # Check bullet collisions
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break

        # Draw player
        pygame.draw.rect(screen, BLUE, player)

        # Draw bullets
        for bullet in bullets:
            pygame.draw.rect(screen, YELLOW, bullet)

        # Draw enemies
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy)

        # Draw score
        draw_text(f"Score: {score}", font, WHITE, 10, 10)

        # Update display
        pygame.display.update()
        clock.tick(FPS)

# Start game
main_game()
pygame.quit()

"""),
("2D Platformer Game", """import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_width, player_height = 50, 50
player_x, player_y = 100, 500
player_speed = 5
player_jump = 15
gravity = 1
velocity_y = 0
is_jumping = False

# Platform settings
platforms = [
    pygame.Rect(50, 550, 200, 20),
    pygame.Rect(300, 450, 200, 20),
    pygame.Rect(550, 350, 200, 20),
    pygame.Rect(150, 250, 200, 20)
]

# Goal settings
goal = pygame.Rect(700, 200, 50, 50)

# Game loop
def main():
    global player_x, player_y, velocity_y, is_jumping

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Keys for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if not is_jumping and keys[pygame.K_SPACE]:
            is_jumping = True
            velocity_y = -player_jump

        # Apply gravity
        if is_jumping:
            velocity_y += gravity
            player_y += velocity_y

        # Check for collision with platforms
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        on_platform = False
        for platform in platforms:
            if player_rect.colliderect(platform) and velocity_y > 0:
                player_y = platform.top - player_height
                velocity_y = 0
                is_jumping = False
                on_platform = True
                break

        # If player falls off platforms
        if not on_platform and not is_jumping:
            is_jumping = True

        # Check if player reaches the goal
        if player_rect.colliderect(goal):
            print("You Win!")
            running = False

        # Draw platforms
        for platform in platforms:
            pygame.draw.rect(screen, BLUE, platform)

        # Draw goal
        pygame.draw.rect(screen, RED, goal)

        # Draw player
        pygame.draw.rect(screen, BLACK, player_rect)

        # Update display
        pygame.display.flip()

        # Limit FPS
        clock.tick(FPS)

if __name__ == "__main__":
    main()

""")

            ],
             
        }

        self.username = None
        self.setup_login_screen()

    def setup_gui(self):
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Configure main frame grid
        self.main_frame.grid_columnconfigure(1, weight=3)  # Center frame gets more weight
        self.main_frame.grid_columnconfigure(2, weight=2)  # Right frame gets less weight
        self.main_frame.grid_rowconfigure(0, weight=1)

        # Create frames
        self.left_frame = ttk.Frame(self.main_frame)
        self.center_frame = ttk.Frame(self.main_frame)
        self.right_frame = ttk.Frame(self.main_frame)

        # Place frames in grid
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.center_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.right_frame.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        # Left frame contents
        ttk.Label(self.left_frame, text="Select Category:").pack(pady=5)
        self.category_var = tk.StringVar(value=list(self.programs.keys())[0])
        self.category_menu = ttk.Combobox(
            self.left_frame,
            textvariable=self.category_var,
            values=list(self.programs.keys()),
            state='readonly'
        )
        self.category_menu.pack(pady=5, fill=tk.X)
        self.category_menu.bind('<<ComboboxSelected>>', self.update_program_list)

        ttk.Label(self.left_frame, text="Select Program:").pack(pady=5)
        self.program_listbox = tk.Listbox(self.left_frame, width=30, height=20)
        self.program_listbox.pack(pady=5, fill=tk.BOTH, expand=True)
        self.program_listbox.bind('<<ListboxSelect>>', self.load_program)

        self.theme_button = ttk.Button(
            self.left_frame,
            text="Toggle Dark Mode",
            command=self.toggle_theme
        )
        self.theme_button.pack(pady=10, fill=tk.X)

        # Center frame contents
        ttk.Label(self.center_frame, text="Code Editor:").pack(anchor='w')
        self.code_editor = scrolledtext.ScrolledText(
            self.center_frame,
            width=80,
            height=25,
            font=('Courier New', 10)
        )
        self.code_editor.pack(fill=tk.BOTH, expand=True, pady=5)

        button_frame = ttk.Frame(self.center_frame)
        button_frame.pack(fill=tk.X, pady=5)
        ttk.Button(button_frame, text="Run Code", command=self.run_code).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_code).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_code).pack(side=tk.LEFT, padx=5)

        ttk.Label(self.center_frame, text="Output:").pack(anchor='w')
        self.output_area = scrolledtext.ScrolledText(
            self.center_frame,
            width=80,
            height=10,
            font=('Courier New', 10)
        )
        self.output_area.pack(fill=tk.BOTH, expand=True, pady=5)

        # Right frame contents
        ttk.Label(self.right_frame, text="Reference Code:").pack(anchor='w')
        self.reference_code_editor = scrolledtext.ScrolledText(
            self.right_frame,
            width=60,
            height=25,
            font=('Courier New', 10)
        )
        self.reference_code_editor.pack(fill=tk.BOTH, expand=True, pady=5)

        # Load initial programs and last code
        self.update_program_list()
        self.load_last_code()

    def setup_login_screen(self):
        # Create a frame to hold both login and register forms
        self.login_frame = ttk.Frame(self.root)
        self.login_frame.pack(pady=100, padx=200)

        # Login form fields
        ttk.Label(self.login_frame, text="Username:").grid(row=0, column=0, pady=10, padx=5)
        self.username_entry = ttk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, pady=10, padx=5)
        
        ttk.Label(self.login_frame, text="Password:").grid(row=1, column=0, pady=10, padx=5)
        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=10, padx=5)
        
        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.register_button = ttk.Button(self.login_frame, text="Register", command=self.show_register)
        self.register_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.register_frame = None

    def show_register(self):
        self.login_frame.destroy()
        self.register_frame = ttk.Frame(self.root)
        self.register_frame.pack(pady=100, padx=200)

        ttk.Label(self.register_frame, text="Username:").grid(row=0, column=0, pady=10, padx=5)
        self.register_username_entry = ttk.Entry(self.register_frame)
        self.register_username_entry.grid(row=0, column=1, pady=10, padx=5)
        
        ttk.Label(self.register_frame, text="Password:").grid(row=1, column=0, pady=10, padx=5)
        self.register_password_entry = ttk.Entry(self.register_frame, show="*")
        self.register_password_entry.grid(row=1, column=1, pady=10, padx=5)
        
        self.register_confirm_button = ttk.Button(self.register_frame, text="Register", command=self.register)
        self.register_confirm_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.back_to_login_button = ttk.Button(self.register_frame, text="Back to Login", command=self.hide_register)
        self.back_to_login_button.grid(row=3, column=0, columnspan=2, pady=10)

    def hide_register(self):
        self.register_frame.destroy()
        self.setup_login_screen()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not self.validate_login(username, password):
            messagebox.showerror("Login Error", "Invalid username or password!")
        else:
            self.username = username
            self.login_frame.destroy()
            self.setup_gui()

    def register(self):
        username = self.register_username_entry.get()
        password = self.register_password_entry.get()
        
        if username and password:
            self.add_user(username, password)
            messagebox.showinfo("Registration Successful", "User registered successfully!")
            self.hide_register()
        else:
            messagebox.showerror("Error", "Please enter a username and password.")

    def validate_login(self, username, password):
        if os.path.exists(self.USER_CREDENTIALS_FILE):
            with open(self.USER_CREDENTIALS_FILE, 'r') as f:
                users = json.load(f)
                return users.get(username) == password
        return False

    def add_user(self, username, password):
        if os.path.exists(self.USER_CREDENTIALS_FILE):
            with open(self.USER_CREDENTIALS_FILE, 'r') as f:
                users = json.load(f)
        else:
            users = {}

        users[username] = password
        
        with open(self.USER_CREDENTIALS_FILE, 'w') as f:
            json.dump(users, f)

    def update_program_list(self, event=None):
        self.program_listbox.delete(0, tk.END)
        category = self.category_var.get()
        for program in self.programs[category]:
            self.program_listbox.insert(tk.END, program[0])

    def load_program(self, event=None):
        selection = self.program_listbox.curselection()
        if selection:
            category = self.category_var.get()
            program_code = self.programs[category][selection[0]][1]
            self.code_editor.delete('1.0', tk.END)
            self.code_editor.insert('1.0', program_code)
            self.reference_code_editor.delete('1.0', tk.END)
            self.reference_code_editor.insert('1.0', program_code)

    def run_code(self):
        code = self.code_editor.get('1.0', tk.END)
        with open('temp_program.py', 'w') as f:
            f.write(code)

        try:
            result = subprocess.run(
                [sys.executable, 'temp_program.py'],
                capture_output=True,
                text=True,
                
            )

            self.output_area.delete('1.0', tk.END)
            if result.stdout:
                self.output_area.insert(tk.END, result.stdout)
            if result.stderr:
                self.output_area.insert(tk.END, "Error:\n" + result.stderr)

        
        except Exception as e:
            self.output_area.delete('1.0', tk.END)
            self.output_area.insert(tk.END, f"Error: {str(e)}")
        finally:
            if os.path.exists('temp_program.py'):
                os.remove('temp_program.py')

    def clear_code(self):
        self.code_editor.delete('1.0', tk.END)
        self.output_area.delete('1.0', tk.END)

    def reset_code(self):
        self.load_program()

    def toggle_theme(self):
        if self.dark_mode:
            self.root.tk_setPalette("white")
            self.dark_mode = False
        else:
            self.root.tk_setPalette("black")
            self.dark_mode = True

    def load_settings(self):
        if os.path.exists(self.SETTINGS_FILE):
            with open(self.SETTINGS_FILE, 'r') as f:
                settings = json.load(f)
                self.timeout = settings.get("timeout", 5)
                self.dark_mode = settings.get("dark_mode", False)

    def load_last_code(self):
        if os.path.exists(self.SETTINGS_FILE):
            with open(self.SETTINGS_FILE, 'r') as f:
                settings = json.load(f)
                last_code = settings.get("last_code", "")
                self.code_editor.insert('1.0', last_code)

    def save_settings(self):
        settings = {
            "timeout": self.timeout,
            "dark_mode": self.dark_mode,
            "last_code": self.code_editor.get('1.0', tk.END).strip()
        }
        with open(self.SETTINGS_FILE, 'w') as f:
            json.dump(settings, f)

    def on_close(self):
        self.save_settings()
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = ProgramPracticeApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()