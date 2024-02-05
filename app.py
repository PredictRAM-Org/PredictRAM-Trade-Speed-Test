import streamlit as st
import random
import time

stocks = ["reliance", "tatamotor", "wipro", "lupin", "adanient", "hdfcbank",
          "axisbank", "sbin", "yesbank", "biocon", "gail", "coalindia",
          "bel", "bhel", "ongc", "itc"]

def generate_random_numbers():
    quantity = random.randint(100, 999)
    price = round(random.uniform(100, 999), 2)
    return quantity, price

def play_game():
    random_stock = random.choice(stocks)
    quantity, price = generate_random_numbers()

    st.write(f"Random stock: {random_stock}")
    st.write(f"Random quantity: {quantity}")
    st.write(f"Random price: {price}")

    st.button("Start Game")

    try:
        entered_quantity = st.number_input("Enter quantity (3 digits):")
        entered_price = st.number_input("Enter price (3 digits):")
    except ValueError:
        st.error("Invalid input. Please enter valid three-digit quantity and price.")
        return 0, 0

    accuracy = 100
    if quantity != entered_quantity:
        st.warning("Incorrect quantity. Deducting accuracy.")
        accuracy -= 10

    if round(price, 2) != round(entered_price, 2):
        st.warning("Incorrect price. Deducting accuracy.")
        accuracy -= 10

    elapsed_time = time.time() - start_time
    st.write(f"Time taken to enter both quantity and price is {elapsed_time:.2f} seconds.")
    st.write(f"Accuracy: {accuracy}%")

    total_cost = entered_quantity * entered_price
    st.write(f"Total cost: {total_cost:.2f}")

    return elapsed_time, accuracy

def main():
    st.title("Stock Game")

    total_time = 0
    total_accuracy = 0
    num_games = 10

    for i in range(num_games):
        st.subheader(f"Game {i + 1}:")
        elapsed_time, accuracy = play_game()
        total_time += elapsed_time
        total_accuracy += accuracy
        st.write("---")

    average_time = total_time / num_games
    average_accuracy = total_accuracy / num_games
    st.write(f"Average time across {num_games} games: {average_time:.2f} seconds")
    st.write(f"Average accuracy across {num_games} games: {average_accuracy:.2f}%")

if __name__ == "__main__":
    main()
