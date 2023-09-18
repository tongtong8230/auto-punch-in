# Punch-In/Punch-Out Automation
This Python script automates the process of punching in and punching out for a specific web application. It uses the Selenium library to interact with the web application's login page and perform the punch-in and punch-out actions.

## Usage
Before running the script, make sure you have Python and the necessary libraries installed.

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/tongtong8230/auto-punch-in.git
   ```

2. Navigate to the project directory:

   ```bash
   cd punch-in
   ```

3. For the first time, run pre-build.sh script to setup username & password:

   ```bash
   ./pre-build.sh
   ```

4. Run the script with one of the following commands:

   To punch in:

   ```bash
   ./run_punchin.sh
   ```

   To punch out:

   ```bash
   ./run_punchoff.sh
   ```

## Requirements

- Python 3.x
- Selenium library 4.12.0
- Google Chrome browser 116.0.X.X (with ChromeDriver) 117.0.X.X

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [Kiki Huang](https://github.com/tongtong8230)
