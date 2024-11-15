import streamlit as st
import random

st.title("Welcome to the Guessing Game")
st.header("Choose your game mode:")

game_mode = st.radio(
    "Select a game mode:",
    ("Human Guessing Number", "Computer Guesses the Number")
)

if game_mode == "Human Guessing Number":
    st.subheader("You need to guess the number between 1 and 100!")

    if 'num' not in st.session_state:
        st.session_state.num = random.randint(1, 100)
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0

    user_guess = st.number_input("Enter a number you have guessed", min_value=1, max_value=100, step=1)

    if st.button("SUBMIT"):
        if st.session_state.attempts < 10:
            st.session_state.attempts += 1
            if user_guess > st.session_state.num:
                st.write("You guessed a number that is too high. Try a smaller number.")
            elif user_guess < st.session_state.num:
                st.write("You guessed a number that is too low. Try a higher number.")
            else:
                st.write(f"Congratulations! You guessed the number correctly in {st.session_state.attempts} attempts!")
                st.balloons()
                st.write("The game will restart.")
                st.session_state.num = random.randint(1, 100)
                st.session_state.attempts = 0
        else:
            st.write("Your attempts are over.")
            st.write(f"The correct number was {st.session_state.num}.")
            st.write("Refresh the screen to restart.")

elif game_mode == "Computer Guesses the Number":
    st.subheader("Think of a number between 1 and 100, and the computer will try to guess it!")

    if 'low' not in st.session_state:
        st.session_state.low = 1
    if 'high' not in st.session_state:
        st.session_state.high = 100
    if 'computer_guess' not in st.session_state:
        st.session_state.computer_guess = random.randint(st.session_state.low, st.session_state.high)
    if 'computer_attempts' not in st.session_state:
        st.session_state.computer_attempts = 0

    st.write(f"Computer's current guess: {st.session_state.computer_guess}")

    choice = st.radio(
        "Is the computer's guess:",
        ("Too High", "Too Low", "Correct")
    )

    if st.button("NEXT"):
        st.session_state.computer_attempts += 1
        if st.session_state.attempts==10:
            st.write("You have failed")
            st.write("Refresh screen to retry")
        elif choice== "Too High":
            st.session_state.high = st.session_state.computer_guess - 1
        elif choice== "Too Low":
            st.session_state.low = st.session_state.computer_guess + 1
        elif choice == "Correct":
            st.write(f"The computer guessed your number correctly in {st.session_state.computer_attempts} attempts!")
            st.balloons()
            st.write("The game will restart.")
            st.session_state.low = 1
            st.session_state.high = 100
            st.session_state.computer_guess = random.randint(1, 100)
            st.session_state.computer_attempts = 0
            st.stop()

        if st.session_state.low <= st.session_state.high:
            st.session_state.computer_guess = random.randint(st.session_state.low, st.session_state.high)
        else:
            st.write("Something went wrong. Please restart the game.")
