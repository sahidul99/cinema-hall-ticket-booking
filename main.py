import uuid
class Star_Cinema:
    def __init__(self) -> None:
        self.hall_list = []
    
    
    def _entry_hall(self,hall):
        self.hall_list.append(hall)
    

class Hall(Star_Cinema):
    def __init__(self,hall_no,rows, cols):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def save(self,cinema):
        cinema._entry_hall(self)

    def entry_show(self,id,movie_name,time):
        show = (id,movie_name,time)
        self.__show_list.append(show)
        arr = [[True]*rows for _ in range(cols)]
        self.__seats[id] = arr

    def book_seats(self,name, phone,show_id, seats):
        ss = ''
        if show_id in self.__seats:
            for seat in seats:
                if self.__seats[show_id][seat[0]][seat[1]]==False:
                    print('One or more seats are booked\n')
                    return
            for seat in seats:
                self.__seats[show_id][seat[0]][seat[1]]=False
                r = chr(ord('A')+seat[0])
                c = seat[1]
                ss+= f' {r}{c}'


            print('\n##### TICKET\'S BOOKED SUCCESSFULLY !! #####')
            print('----------------------------------------------')
            print(f'NAME: {name} \nPHONE NO: {phone}\n\n')
            for show in self.__show_list:
                if show[0] == show_id:
                    sh = show
            print(f'MOVIE NAME: {sh[1]}\tMOVIE TIME: {sh[2]}')
            print(f'SEATS: {ss}')
            print(f'HALL:{self.__hall_no}')
            print('----------------------------------------------\n')
            
        else:
            print('Invalid show ID')

    def view_show_list(self):
        print('---------------------------------------------------------------')
        print('SHOW ID\t\tMOVIE NAME\t\tTIME\n')
        for show in self.__show_list:
            print(f'{show[0]}\t\t{show[1]}\t\t{show[2]}')
        print('----------------------------------------------------------------\n')
    def view_available_seats(self,id):
        
        if str(id) in self.__seats:
            for movie in self.__show_list:
                if movie[0] == str(id):
                    sel = movie
                    break
            print('\n\n')
            print(f'MOVIE NAME: {sel[1]} \tTIME: {sel[2]}')
            print('\n\tBooked seats are marked as X')
            print('-------------------------------------------------------')
            char = 'A'
            num = 0
            for row in self.__seats[str(id)]:
                for col in row:
                    if col:
                        print(f'{char}{num}',end='\t')
                    else:
                        print('X', end='\t')
                    num+=1
                print('\n')
                num = 0
                char = chr(ord(char)+1)
            print('---------------------------------------------------------\n')
        else:
            print('Invalid show id\n')
                    

cinema = Star_Cinema()

hall_no = str(uuid.uuid4().fields[-1])[:5]
rows = 3
cols = 4
hall = Hall(hall_no,rows,cols)
hall.save(cinema)





id1 = str(uuid.uuid4().fields[-1])[:5]
id2 = str(uuid.uuid4().fields[-1])[:5]
movie_name1 = 'Sample movie 1'
movie_name2 = 'sample movie 2'
movie_time = '12/2/2022 11:30 PM'
hall.entry_show(id1,movie_name1,movie_time)
hall.entry_show(id2,movie_name2,movie_time)

# print(cinema.hall_list[0].view_show_list())

while(True):
    print('1. VIEW ALL SHOWS TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    print('4. EXIT')
    print('\n')
    choice1 = int(input('ENTER OPTION: '))

    if choice1 == 1:
        hall.view_show_list()
    elif choice1 == 2:
        choice2 = int(input('ENTER SHOW ID: '))
        # print(choice2)
        hall.view_available_seats(choice2)
    elif choice1 == 3:
        name = input('ENTER CUSTOMER NAME: ')
        phone = input('ENTER CCUSTOMER PHONE NUMBER: ')
        id = input('ENTER SHOW ID: ')
        seats = []
        n = int(input('ENTER NUMBER OF SEATS: '))
        if n>rows*cols:
            print('Not enough seats')
        else:
            seat_list = input('ENTER SEATS: ').split(' ')
            for seat in seat_list: # seat = A1 B1
                r = ord(seat[0])-ord('A')
                c = int(seat[1])
                if r>rows-1 or rows<1 or c>cols or c<0:
                    print('INVALID SEAT SELECTION, TRY AGAIN')
                    continue
                t = (r,c)
                seats.append(t)
                if seat_list[n-1] == seat:
                    break
            hall.book_seats(name,phone,id,seats)
    elif choice1 == 4:
        break
    else:
        print('INVALID SELECTION, TRY AGAIN\n')
