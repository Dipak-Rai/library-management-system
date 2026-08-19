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
    try:
        file_name = input("Enter file name to add book: ")  
        
        # check file if not found
        if not file_name:
            print("Sorry! file name cannot be empty")
            return
        
        path = Path(file_name)
        
        # Check extension of file if user not enter extension it allow to make .txt autometically
        if path.suffix == "":
            path = path.with_suffix(".txt")
                    
                    
        # If file name does not exist
        if not path.exists():
            print(f"Sorry! {path} file does not exist")
            return
        
        
        # Check whether path is actually a file
        if not path.is_file():
            print(f"Error! {path} is not a valid file")
            return
        
        
        # Get book information     
        book_id = input("Enter book ID: ").strip()
        if not book_id:
            print("Error! book Id cannot be empty.")
            return
        
        #check duplicate ID in book list file:
        with open(path, 'r') as file:
            for line in file:
                info = line.strip().split(',')
                if info[0].strip() == book_id.strip():
                    print(f"Error! Book ID '{book_id}' already exist.")
                    return
                
        book_title = input("Enter book title: ").strip()
        if not book_title:
            print("Error! Book title cannot be empty.")
            return
        
        book_author = input("Enter Author name: ").strip()
        if not book_author:
            print("Error! Book title cannot be empty.")
            return
        
        book_category = input("Enter book category: ").strip()
        if not book_category:
            print("Error! Book title cannot be empty.")
            return
        
        #Validate price:
        try:
            book_price = float(input("Enter book price: ").strip())
            if book_price<0:
                print("Error! Book price cannot be negative")
                return
        except ValueError:
            print("Error! Enter valid number for price")
        
        # Valid quantity
        try:    
            book_quantity = int(input("Enter book quantity: ").strip())
            if book_quantity<0:
                print("Error! Book quantity cannot be negatinve")
                return
        except ValueError:
            print("Error! Please enter valid quantity")
        
                
        book_item = (
            f"{book_id}, {book_title}, {book_author}, {book_category}, {book_price}, {book_quantity}"
            )
                
        with open(path, 'w') as file:
            file.write(book_item)
        print(f"Book '{book_title}' added successfully")
    except PermissionError:
        print("Error! you do not have permission to add book list")
        
    except OSError as err:
        print(f"File system error: {err}")
        
    except Exception as err:
        print(f"Unexpected error: {err}")

def view_book():
    try:
        file_name = input("Enter book file name to view list: ").strip()
        
        # If user not enter file name
        if not file_name:
            print("Error! File name cannot be empty.")
            return
        
        path = Path(file_name)
        
        # User can enter file name without extension (.txt)
        if path.suffix == "":
            path = path.with_suffix(".txt")
        
        # Check file not exist
        if not path.exists():
            print(f"Error! {path} does not exist.")
            return
            
        # Check whether is this file
        if not path.is_file():
            print(f"Error! {path} is not a file")
            return
        
        # If file exist:
        found = False
        if path.exists():
            with open(path, 'r') as file:
                for line in file:
                    info = line.strip().split(',')
                    if len(info)<6:
                        print("Warning! invalid book record found.")
                        continue
                    
                    found=True
                    print("\n===============================")
                    print("Library Books")
                    print("===============================")
                    print(
                        f"Book ID       : {info[0]}\n"
                        f"Title         : {info[1]}\n"
                        f"Author        : {info[2]}\n"
                        f"Category      : {info[3]}\n"
                        f"Price         : Rs.{info[4]}\n"
                        f"Quantity      : {info[5]}"
                        
                    )
                    
        if found:
            print("\n Library books viewed successfully.")
        else:
            print("\n Sorry! No books record found")
            
    except PermissionError:
        print("Error! You don't have permission to read this file")
    except OSError as err:
        print(f"Error! File system error: {err}")
        
        

def search_book():
    try:
        file_name = input("Enter file name to search book: ").strip()
        
        #check file name empty:
        if not file_name:
            print("Error! file name can't be empty.")
            return
        
        # user can used file name without using extension '.txt'
        path = Path(file_name)
        if path.suffix == "":
            path = path.with_suffix(".txt")
            
        # Check file path if not exist
        if not path.exists():
            print(f"Error! {path} file has not exist.")
            return
        
        # Check is this file.
        if not path.is_file():
            print(f"Error! {path} is not a file")
            return
        
        # if path exist: 
        found = False
        if path.exists():
            book_id = input("Enter book id for search: ").strip()
            
            # check book id
            if not book_id:
                print("Error! Book ID cannot be empty.")
                return
            
            with open(path, 'r') as file:
                book_items = file.readlines()
                
                for line in book_items:
                    info = line.strip().split(',')
                    # skip empty line
                    if not line.strip():
                        continue
                    
                    # Check valid book record
                    if len(info)<6:
                        print("Warning! Invalid book record found.")
                        continue
                    
                    if info[0].strip() == book_id.strip():
                        found = True
                        
                        print("\n=================================")
                        print(f"'{info[1]}' book is found")
                        print("===================================")
                        print(
                            f"Book ID       : {info[0]}\n"
                            f"Title         : {info[1]}\n"
                            f"Author        : {info[2]}\n"
                            f"Category      : {info[3]}\n"
                            f"Price         : Rs.{info[4]}\n"
                            f"Quantity      : {info[5]}"
                        )
                        break
        if found:
            print(f" found successfully.")
        else:
            print("Error! Such book has not exist.")
    except PermissionError:
        print("Error! You don't have permission to search book.")
    except OSError as err:
        print(f"Sorry! File system error: {err}")

def update_book():
    file_name = input("Enter file name for update: ").strip()
    
    # If file name is empty:
    if not file_name:
        print("Error! File name should not be empty.")
        return
    
    path = Path(file_name)
    
    # User can enter without use extension
    if path.suffix==(""):
        path = path.with_suffix(".txt")
        
    
    # If path not exist:
    if not path.exists():
        print("Error! Such file has not exist.")
        return
    
    # If path file is not exist
    if not path.is_file():
        print("Error! file name is not a file ")
        return
    
    # If path Exist
    found = False
    if path.exists():
        book_id = input("Enter book id for update: ").strip()
        
        # if ID is empty
        if not book_id:
            print("Error! ID should not be empty.")
            return
        
        with open(path, 'r') as file:
            book_items = file.readlines()
            for index, line in enumerate(book_items):
                book_item = line.strip().split(',')
                
                #Skip empty line
                if not book_item:
                    continue
                
                #validate book record
                if len(book_item)<6:
                    print("Warning! invalid book record found")
                    continue
                
                #check book id
                if book_item[0].strip()==book_id.strip():
                    found = True
                    print("\n=============================")
                    print(f"{book_item[1]} Book List")
                    print("\n=============================")
                    print(
                        f"Book ID       : {book_item[0]}\n"
                        f"Title         : {book_item[1]}\n"
                        f"Author        : {book_item[2]}\n"
                        f"Category      : {book_item[3]}\n"
                        f"Price         : Rs.{book_item[4]}\n"
                        f"Quantity      : {book_item[5]}"
                    )
                    
                    print("\n================================")
                    print("Update book ")
                    print("Enter new information")
                    print("================================")
                    
                    # if check input are empty
                    book_title = input("Update book title: ").strip()
                    if not book_title:
                        print("Error! Book tile should not be empty")
                        return
                    
                    book_author = input("Update book author name: ").strip()
                    if not book_author:
                        print("Error! Book author name should not be empty")
                        return
                    
                    book_category = input("Update book category: ").strip()
                    if not book_category:
                        print("Error! Book category should not be empty")
                        return
                    
                    # valid price 
                    try:
                        book_price = float(input("Update book price").strip())
                        if book_price<0:
                            print("Error! price is not a negative number.")
                            return
                    except ValueError:
                        print("Error! enter a valid number.")
                    
                    # Quantity validation
                    try:
                        book_quantity = int(input("Update book quentity: ").strip())
                        if book_quantity<0:
                            print("Error! quantity is not a negative number.")
                            return
                    except ValueError:
                        print("Error! enter a valid number")
                    
                    book_items[index] = (
                        f"{book_id}, {book_title}, {book_author}, {book_category}, {book_price}, {book_quantity}"
                    )
                    break
    if found:
        with open(path, 'w') as file:
            file.writelines(book_items)
        print(f"\n Book Id '{book_item[1]}' book updated successfully")
        
    else:
        print("Error! such book id does not exist.")
        
        
                
                    
                    
                    
                    
                    
                    
                    
                    
        
    

                
                
            
    



while True:
    print("\n Library Management System")
    print("==============================")
    print("1. Create Book File")
    
    print("2. Add Book")
    print("3. view Book")
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
    