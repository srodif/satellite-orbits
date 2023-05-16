

def create_time_graph():
    # Sample time values and altitude values
    time_values = [0]
    height = 500000
    drag_coeff = 2.2
    cross_area = 25
    mass = 1000
    
    # Calling the function to calculate heights
    heights = calculate_heights(time_values, height, drag_coeff, cross_area, mass)
    
    # Printing the calculated heights
    for t, h in zip(time_values, heights):
        print("At time", t, "seconds, the height is", h, "meters")
    
    plt.plot(time_values, heights)
    plt.xlabel('Time Elapsed (s)')
    plt.ylabel('Height (m)')
    plt.title('Satellite Height vs Time')
    plt.show()


#main programm sequence run
while True:
    print("")
    time.sleep(1)
    print("Please select an option:")
    print("1. Enter data, calculate values, and print them")
    print("2. Print graphs")
    print("3. Create time - height graph")
    print("4. Print all data")
    print("5. Delete data values")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        calculate_satellite_parameters()
    elif choice == "2":
        make_graphs()
    elif choice == "3":
        create_time_graph()
    elif choice == "4":
        print(data)
    elif choice == "5":
        delete_data()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
print("Program end")