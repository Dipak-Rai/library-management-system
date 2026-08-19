from pathlib import Path

def create_book_file():
    try:
        #add name to create file 
        book_file = input("Enter book file name: ")
        
        # check file name
        if not book_file:
            print("Error! file name cannot be empty.")
            return
        
        # create path to store file    
        path = Path(book_file)
        
        # Check if file exist cannot create twice same file name
        if path.exists():
            if path.is_file():
                print(f"Sorry! {path} is already exist.")
            else:
                print(f"Sorry! {path} is not a file.")
                return
        
        # if file does not exist user allow to create file 
        else:
            # Create .txt file extension if user not provide extension.
            if path.suffix == "":
                path = path.with_suffix(".txt")
            
            # Create file
            with open(path, 'w') as file:
                file.write()
                pass
            
    except PermissionError:
        print("Error! you do have permission to create this file.")
        
    except OSError as err:
        print(f"File system error: {err}")
        
    except Exception as err:
        print(f"unexpected error: {err}")
    
def add_book():
    file_name = input("Enter file name to add book: ")  
    
    # check file if not found
    if not file_name:
        print("Sorry! file name cannot be empty")
        return
    
    path = Path(file_name)
    
    # If file name does not exist
    if not path.exists():
        print(f"Sorry! {path} file does not exist")
        return
    
    # if file name exist user allow to add book information:
    if path.exists():
        
        # Check extension of file if user not enter extension it allow to make .txt autometically
        if path.suffix == "":
            path = path.with_suffix(".txt")
            
            book_id = input("Enter book ID: ").strip()
            book_title = input("Enter book title: ").strip()
            book_author = input("Enter Author name: ").strip()
            book_category = input("Enter book category: ").strip()
            book_price = int(input("Enter book price: ").strip())
            book_quantity = int(input("Enter book quantity: ").strip())
            
            
        
    
    
    
    


while True:
    print("\n Library Management System")
    print("==============================")
    print("1. Create Book File")
    
    print("2. Add Book")
    print("3. Search Book")
    print("4. Search Book")
    print("5. Update Book")
    print("6. Delete Book")
    
    print("7. Create Member File")
    print("8. Add Member")
    print("9. View Members")
    print("10. Search Member")
    print("11. Update Member")
    print("12. Delete Member")
    
    
    print("13. Create Borrow File")
    print("14. Borrow Book")
    print("15. View Borrowed Books")
    print("16. Search Borrow Record")
    print("17. Return Book")
    print("18. Delete Borrow Record")
    
    print("19. Library Summery")
    print("Exit")
    
    choice = int(input("Please enter number what you want to do: ").strip())
    
    if choice == 1:
        create_book_file()
    
    elif choice == 2:
        add_book()
    
    elif choice == 3:
        view_book()
    
    elif choice == 4:
        search_book()
    
    elif choice == 5:
        update_book()
    
    elif choice == 6:
        delete_book()
        
        
    else:
        print("Sorry! Such function does not found.")
    