import tkinter as tk
import importlib

def run_curls_detection(left_reps, right_reps):

    global feedback_label
    try:
        left_reps = int(left_reps)
        right_reps = int(right_reps)
        externalCode = importlib.import_module("Exercises.Curls")
        externalCode.run_curls_detection(left_reps, right_reps)
        feedback_label.config(text="", fg="black")
    except ValueError:
        feedback_label.config(text="Please enter valid number of repetitions.", fg="red")
        left_reps_entry.delete(0, tk.END)
        right_reps_entry.delete(0, tk.END)

def run_squats_detection(repetitions):

    global feedback_label
    try:
        repetitions = int(repetitions)
        externalCode = importlib.import_module("Exercises.Squats")
        externalCode.run_squats_detection(repetitions)
        feedback_label.config(text="", fg="black")
    except ValueError:
        feedback_label.config(text="Please enter valid number of repetitions.", fg="red")
        reps_entry.delete(0, tk.END)

def run_russianTwists_detection(reps):

    global feedback_label
    try:
        reps = int(reps)
        externalCode = importlib.import_module("Exercises.RussianTwists")
        externalCode.run_russianTwists_detection(reps)
        feedback_label.config(text="", fg="black")
    except ValueError:
        feedback_label.config(text="Please enter valid number of repetitions.", fg="red")
        russian_twists_reps_entry.delete(0, tk.END)

def run_pushUps_detection(pReps):

    global feedback_label
    try:
        pReps = int(pReps)
        externalCode = importlib.import_module("Exercises.PushUps")
        externalCode.run_pushUps_detection(pReps)
        feedback_label.config(text="", fg="black")
    except ValueError:
        feedback_label.config(text="Please enter valid number of repetitions.", fg="red")
        pushUps_reps_entry.delete(0, tk.END)

def run_sideLunges_detection(left_lreps, right_lreps):

    global feedback_label
    try:
        left_lreps = int(left_lreps)
        right_lreps = int(right_lreps)
        externalCode = importlib.import_module("Exercises.SideLunges")
        externalCode.run_sideLunges_detection(left_lreps, right_lreps)
        feedback_label.config(text="", fg="black")
    except ValueError:
        feedback_label.config(text="Please enter valid number of repetitions.", fg="red")
        left_lunges_entry.delete(0, tk.END)
        right_lunges_entry.delete(0, tk.END)

def run_jumping_jacks_detection(jj_reps):

    global feedback_label
    try:
        jj_reps = int(jj_reps)
        externalCode = importlib.import_module("Exercises.JumpingJacks")
        externalCode.run_jumpingJacks_detection(jj_reps)
        feedback_label.config(text="", fg="black")
    except ValueError:
        feedback_label.config(text="Please enter valid number of repetitions.", fg="red")
        jj_reps_entry.delete(0, tk.END)

def run_plank_detection(duration):

    global feedback_label
    try:
        duration = int(duration)
        externalCode = importlib.import_module("Exercises.Plank")
        externalCode.run_plank_detection(duration)
        feedback_label.config(text="", fg="black")
    except ValueError:
        feedback_label.config(text="Please enter a valid duration in seconds.", fg="red")
        duration_entry.delete(0, tk.END)

def run_selected_exercise(selected_exercise, left_reps, right_reps, squats_reps, russian_twists_reps, pushUps_reps,
                          left_lunges, right_lunges, jj_reps, duration):

    if selected_exercise.get() == "Curls":
        run_curls_detection(left_reps, right_reps)
    elif selected_exercise.get() == "Squats":
        run_squats_detection(squats_reps)
    elif selected_exercise.get() == "Russian Twists":
        run_russianTwists_detection(russian_twists_reps)
    elif selected_exercise.get() == "Push-Ups":
        run_pushUps_detection(pushUps_reps)
    elif selected_exercise.get() == "Side Lunges":
        run_sideLunges_detection(left_lunges, right_lunges)
    elif selected_exercise.get() == "Jumping Jacks":
        run_jumping_jacks_detection(jj_reps)
    elif selected_exercise.get() == "Plank":
        run_plank_detection(duration)
    else:
        feedback_label.config(text="Unknown exercise selected.", fg="orange")

def update_ui(selected_exercise):

    for widget in input_frame.winfo_children():
        widget.pack_forget()

    if selected_exercise.get() == "Squats":
        reps_label.pack(pady=10)
        reps_entry.pack(pady=10)
        left_reps_label.pack_forget()
        left_reps_entry.pack_forget()
        right_reps_label.pack_forget()
        right_reps_entry.pack_forget()
        russian_twists_reps_label.pack_forget()
        russian_twists_reps_entry.pack_forget()
        pushUps_reps_label.pack_forget()
        pushUps_reps_entry.pack_forget()
        left_lunges_label.pack_forget()
        left_lunges_entry.pack_forget()
        right_lunges_label.pack_forget()
        right_lunges_entry.pack_forget()
        jj_reps_label.pack_forget()
        jj_reps_entry.pack_forget()
        duration_label.pack_forget()
        duration_entry.pack_forget()
    elif selected_exercise.get() == "Curls":
        left_reps_label.pack(pady=10)
        left_reps_entry.pack(pady=10)
        right_reps_label.pack(pady=10)
        right_reps_entry.pack(pady=10)
        reps_label.pack_forget()
        reps_entry.pack_forget()
        russian_twists_reps_label.pack_forget()
        russian_twists_reps_entry.pack_forget()
        pushUps_reps_label.pack_forget()
        pushUps_reps_entry.pack_forget()
        left_lunges_label.pack_forget()
        left_lunges_entry.pack_forget()
        right_lunges_label.pack_forget()
        right_lunges_entry.pack_forget()
        jj_reps_label.pack_forget()
        jj_reps_entry.pack_forget()
        duration_label.pack_forget()
        duration_entry.pack_forget()
    elif selected_exercise.get() == "Russian Twists":
        russian_twists_reps_label.pack(pady=10)
        russian_twists_reps_entry.pack(pady=10)
        reps_label.pack_forget()
        reps_entry.pack_forget()
        left_reps_label.pack_forget()
        left_reps_entry.pack_forget()
        right_reps_label.pack_forget()
        right_reps_entry.pack_forget()
        pushUps_reps_label.pack_forget()
        pushUps_reps_entry.pack_forget()
        left_lunges_label.pack_forget()
        left_lunges_entry.pack_forget()
        right_lunges_label.pack_forget()
        right_lunges_entry.pack_forget()
        jj_reps_label.pack_forget()
        jj_reps_entry.pack_forget()
        duration_label.pack_forget()
        duration_entry.pack_forget()
    elif selected_exercise.get() == "Push-Ups":
        pushUps_reps_label.pack(pady=10)
        pushUps_reps_entry.pack(pady=10)
        reps_label.pack_forget()
        reps_entry.pack_forget()
        left_reps_label.pack_forget()
        left_reps_entry.pack_forget()
        right_reps_label.pack_forget()
        right_reps_entry.pack_forget()
        russian_twists_reps_label.pack_forget()
        russian_twists_reps_entry.pack_forget()
        left_lunges_label.pack_forget()
        left_lunges_entry.pack_forget()
        right_lunges_label.pack_forget()
        right_lunges_entry.pack_forget()
        jj_reps_label.pack_forget()
        jj_reps_entry.pack_forget()
        duration_label.pack_forget()
        duration_entry.pack_forget()
    elif selected_exercise.get() == "Side Lunges":
        left_lunges_label.pack(pady=10)
        left_lunges_entry.pack(pady=10)
        right_lunges_label.pack(pady=10)
        right_lunges_entry.pack(pady=10)
        reps_label.pack_forget()
        reps_entry.pack_forget()
        russian_twists_reps_label.pack_forget()
        russian_twists_reps_entry.pack_forget()
        pushUps_reps_label.pack_forget()
        pushUps_reps_entry.pack_forget()
        jj_reps_label.pack_forget()
        jj_reps_entry.pack_forget()
        duration_label.pack_forget()
        duration_entry.pack_forget()
    elif selected_exercise.get() == "Jumping Jacks":
        jj_reps_label.pack(pady=10)
        jj_reps_entry.pack(pady=10)
        reps_label.pack_forget()
        reps_entry.pack_forget()
        left_reps_label.pack_forget()
        left_reps_entry.pack_forget()
        right_reps_label.pack_forget()
        right_reps_entry.pack_forget()
        russian_twists_reps_label.pack_forget()
        russian_twists_reps_entry.pack_forget()
        pushUps_reps_label.pack_forget()
        pushUps_reps_entry.pack_forget()
        left_lunges_label.pack_forget()
        left_lunges_entry.pack_forget()
        right_lunges_label.pack_forget()
        right_lunges_entry.pack_forget()
        duration_label.pack_forget()
        duration_entry.pack_forget()
    elif selected_exercise.get() == "Plank":
        duration_label.pack(pady=10)
        duration_entry.pack(pady=10)
        reps_label.pack_forget()
        reps_entry.pack_forget()
        left_reps_label.pack_forget()
        left_reps_entry.pack_forget()
        right_reps_label.pack_forget()
        right_reps_entry.pack_forget()
        russian_twists_reps_label.pack_forget()
        russian_twists_reps_entry.pack_forget()
        pushUps_reps_label.pack_forget()
        pushUps_reps_entry.pack_forget()
        left_lunges_label.pack_forget()
        left_lunges_entry.pack_forget()
        right_lunges_label.pack_forget()
        right_lunges_entry.pack_forget()
        jj_reps_label.pack_forget()
        jj_reps_entry.pack_forget()

    button.pack(pady=20)

def stop_exercise(event):

    global is_stopped
    is_stopped = True
    feedback_label.config(text="Exercise stopped.", fg="orange")

def create_gui():

    global root, feedback_label, button
    global left_reps_entry, right_reps_entry, left_reps_label, right_reps_label
    global reps_entry, reps_label, selected_exercise, russian_twists_reps_entry, russian_twists_reps_label
    global pushUps_reps_entry, pushUps_reps_label, is_stopped
    global left_lunges_entry, right_lunges_entry, left_lunges_label, right_lunges_label
    global jj_reps_entry, jj_reps_label
    global duration_entry, duration_label

    is_stopped = False

    root = tk.Tk()
    root.title("Fitness App")
    root.geometry("1200x700")
    root.configure(bg="#D2B48C")
    root.config(cursor="hand2")

    label = tk.Label(root, text="Select the exercise and press the button to start.", fg="#C2B280", bg="black",
                     font=("Arial", 20, "bold", "italic"))
    label.pack(pady=20)

    global input_frame
    input_frame = tk.Frame(root)
    input_frame.pack(pady=20)

    selected_exercise = tk.StringVar(root)
    selected_exercise.set("Select an exercise")

    exercise_menu = tk.OptionMenu(root, selected_exercise, "Curls", "Squats", "Russian Twists", "Push-Ups",
                                  "Side Lunges", "Jumping Jacks", "Plank",
                                  command=lambda _: update_ui(selected_exercise))
    exercise_menu.config(bg="#D4C2A1", font=("Arial", 14))
    exercise_menu.pack(pady=20)

    reps_label = tk.Label(root, text="Enter number of repetitions for squats:")
    reps_label.config(bg="#D2B48C", font=("Arial", 14))
    reps_entry = tk.Entry(root, font=("Arial", 14), bg="#D4C2A1")

    left_reps_label = tk.Label(root, text="Enter number of repetitions for left arm:")
    left_reps_label.config(bg="#D2B48C", font=("Arial", 14))
    left_reps_entry = tk.Entry(root, font=("Arial", 14), bg="#D4C2A1")

    right_reps_label = tk.Label(root, text="Enter number of repetitions for right arm:")
    right_reps_label.config(bg="#D2B48C", font=("Arial", 14))
    right_reps_entry = tk.Entry(root, font=("Arial", 14), bg="#D4C2A1")

    russian_twists_reps_label = tk.Label(root, text="Enter number of repetitions for Russian Twists:")
    russian_twists_reps_label.config(bg="#D2B48C", font=("Arial", 14))
    russian_twists_reps_entry = tk.Entry(root, font=("Arial", 14), bg="#D4C2A1")

    pushUps_reps_label = tk.Label(root, text="Enter number of repetitions for Push-Ups:")
    pushUps_reps_label.config(bg="#D2B48C", font=("Arial", 14))
    pushUps_reps_entry = tk.Entry(root, font=("Arial", 14), bg="#D4C2A1")

    left_lunges_label = tk.Label(root, text="Enter number of repetitions for left lunges:")
    left_lunges_label.config(bg="#D2B48C", font=("Arial", 14))
    left_lunges_entry = tk.Entry(root, font=("Arial", 14), bg="#D4C2A1")

    right_lunges_label = tk.Label(root, text="Enter number of repetitions for right lunges:")
    right_lunges_label.config(bg="#D2B48C", font=("Arial", 14))
    right_lunges_entry = tk.Entry(root, font=("Arial", 14), bg="#D4C2A1")

    jj_reps_label = tk.Label(root, text="Enter number of repetitions for Jumping Jacks:")
    jj_reps_label.config(bg="#D2B48C", font=("Arial", 14))
    jj_reps_entry = tk.Entry(root, font=("Arial", 14), bg="#D4C2A1")

    duration_label = tk.Label(root, text="Enter duration for Plank in seconds:")
    duration_label.config(bg="#D2B48C", font=("Arial", 14))
    duration_entry = tk.Entry(root, font=("Arial", 14), bg="#D4C2A1")

    feedback_label = tk.Label(root, text="", fg="black", bg="#D2B48C", font=("Arial", 14))
    feedback_label.pack(pady=10)

    button = tk.Button(root, text="Start Exercise", command=lambda: run_selected_exercise(selected_exercise,
                                                                                          left_reps_entry.get(),
                                                                                          right_reps_entry.get(),
                                                                                          reps_entry.get(),
                                                                                          russian_twists_reps_entry.get(),
                                                                                          pushUps_reps_entry.get(),
                                                                                          left_lunges_entry.get(),
                                                                                          right_lunges_entry.get(),
                                                                                          jj_reps_entry.get(),
                                                                                          duration_entry.get()),
                       bg="#C2B280", font=("Arial", 16))

    root.bind("<Escape>", stop_exercise)

    root.mainloop()

create_gui()
