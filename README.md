# **BGMI (Erangel) Map Location Guessing Game** 🛪️

## **Project Description**
This is an interactive guessing game built using Python's **Turtle Graphics** and **Pandas** library. Players are challenged to guess specific locations on the *Erangel* map (a famous map inspired by PUBG). When a player types a correct location, the name appears on the map in its corresponding coordinates. The goal is to guess all the locations before exiting the game.

---

## **How the Game Works**
1. The game displays the Erangel map as the background.
2. The player types the names of locations in the input box.
3. Correct guesses are displayed on the map at their respective positions.
4. If the player types "Exit", the game ends, and it shows the locations that were missed.
5. The game continues until the player guesses all locations or exits.

---

## **Features**
- Interactive map-based game using **Turtle Graphics**.
- Tracks correctly guessed locations.
- Displays missed locations at the end of the game.
- Simple and fun way to test your knowledge of the Erangel map.

---

## **Game Screenshots**
### Starting the Game
![Game Start](https://github.com/dbmurali/BGMI_location_guessing/blob/bd8897a6a511dc1450c50c8eeaed1f5ec0eb49f6/Start%20Screen.png)

### Correct Guess
![Correct Guess](https://github.com/dbmurali/BGMI_location_guessing/blob/bd8897a6a511dc1450c50c8eeaed1f5ec0eb49f6/currect%20guess.png)

### End of the Game
![Game Over](https://github.com/dbmurali/BGMI_location_guessing/blob/bd8897a6a511dc1450c50c8eeaed1f5ec0eb49f6/Game%20Over.png)

---

## **Installation**

Follow these steps to run the project locally:

1. **Clone the Repository**  
   Open your terminal and run:
   ```bash
   git clone https://github.com/yourusername/erangel-guessing-game.git
   ```

2. **Install Required Libraries**  
   Install the required Python libraries using `pip`:
   ```bash
   pip install pandas turtle
   ```

3. **Prepare Your Map and Location Data**  
   - **new_erangel.gif**: Make sure you have the Erangel map image in `.gif` format.  
   - **list_of_place.csv**: A CSV file with the location names and their x, y coordinates. The CSV format must be:
     ```csv
     place,x,y
     Pochinki,100,-150
     School,200,-50
     ```

4. **Run the Game**  
   Execute the Python script:
   ```bash
   python main.py
   ```

---

## **File Structure**
```
.
|-- main.py                # Main game script
|-- new_erangel.gif        # Erangel map image
|-- list_of_place.csv      # Location names with coordinates
|-- images/                # Screenshots for README
|-- README.md              # Project documentation
```

---

## **How to Play**
1. Start the game by running the script.
2. Type the names of Erangel locations into the input box (e.g., "Pochinki", "School", etc.).
3. Correct guesses will display the name on the map at the correct position.
4. Type **Exit** to end the game and see which locations were missed.

---

## **Technologies Used**
- **Python**: Programming language used for the game logic.
- **Turtle Graphics**: To display the map and write locations interactively.
- **Pandas**: To read and manage location data from a CSV file.

---

## **Example CSV File (`list_of_place.csv`)**
```csv
place,x,y
Pochinki,100,-150
School,200,-50
Rozhok,50,70
Mylta,-100,-200
```

---

