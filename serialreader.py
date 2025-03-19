import time
import serial
import csv

SERIAL_PORT = 'COM3' # change using Device Manager with arduino plugged in
BAUD_RATE = 9600

# CSV file name - change based on which dataset we are collecting for
csv_filename = "running.csv"

def main():
  try:
    # open serial port
    print(f"Opening serial port {SERIAL_PORT}...")
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print("Serial port opened successfully!\n")

    time.sleep(2) # give arduino time to reset

    # open CSV file
    with open(csv_filename, 'a', newline='') as csvfile:
      csv_writer = csv.writer(csvfile)

      print(f"Logging data to {csv_filename}. Press Ctrl+C to stop logging.")

      while True:
        line = ser.readline().decode('utf-8').strip() # converts the bytes sent by Arduino into readable string

        if line:
          data = line.split(',')
          csv_writer.writerow(data) # write to csv
          csvfile.flush() # ensures data is written to disk


  except KeyboardInterrupt:
    print("\nLogging stopped.")
  except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
  finally:
    if 'ser' in locals() and ser.is_open:
      ser.close()
      print("Serial port closed.")

    print(f"Data appended to {csv_filename}")

if __name__ == "__main__":
  main()
