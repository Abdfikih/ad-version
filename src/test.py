from database import DATABASE  # Mengimpor class DATABASE dari file database.py

def main():
    # Membuat instance dari DATABASE
    db = DATABASE()

    # Menyambung ke InfluxDB
    if db.connect():
        print("Connected to InfluxDB successfully.")
        
        # Mengatur measurement jika diperlukan
        db.meas = "UEReports"  # Gantilah dengan nama measurement yang relevan

        # Membaca data
        print("Reading data...")
        db.read_data(train=True, limit=1000)  # Atur parameter sesuai kebutuhan
        print("Data read from InfluxDB:")
        print(db.data)

    else:
        print("Failed to connect to InfluxDB.")

if __name__ == "__main__":
    main()
