def datatypes():
  # name = input('What is your name?\n')
  # print("Hello " + name)

  # Data Types

  # int
  print(f'Data type of 3 : {type(3)}')
  print(f'Data type of 0 : {type(0)}')

  # float
  print(f'Data type of 0.0 : {type(0.0)}')

  # bool
  print(f"Data type of 'True' :  {type(True)}")

  # str are the immuatible data type
  print(f"Data type of 'rafi' : {type('rafi')}")

  # long str
  long_str = '''
  000
  111
  333'''
  print(f"value of long string i.e, writing in multi lines : {long_str}")
  
  # list
  list_numbers = [1,'a',3.534,4,5,True]
  print(f"list values : {list_numbers}")
  # list slicing are creates an new copy of the list
  print(f"list of slicing : {list_numbers[0:2]}")
  # list unpackig
  a,b,c,*all,d = [1,'a',3.534,4,5,True,6,7,8,9,10]
  print(f"\nAfter unpacking the list\na -> {a} \nb -> {b} \nc -> {c} \nall -> {all} \nd -> {d} \n ")

  # matrix are the 2D arrarys or 3D arrays 
  matrix =[
    [1,2,4,5],
    [6,7,8,9],
    [10,11,12,13]
    ]
  print(f"Value of Matrix : {matrix}")
  # finding an value in matrix 'matrix_name[colum][row]'
  print(f"Value of Matrix at row->1, colum->3 : {matrix[0][2]}")

  # Tuple are the immuatable
  my_tuple = (1,2,3,4)
  print(f"Tuple : {my_tuple}")
  
  # set
  my_set = {1,2,3,4,5,5,5,5,6,6,7,7,1}
  print(f"Set : {my_set}")

  # dictionary
  dictionary = {'a':1,'b':2}
  print(f"\nDictionary : {dictionary}")

  # None

  # complex a+ib where, a,b are the number i -> j
  print(f"Data type of 3+6i : {type(3+6j)}")

  # converting the integer number into binary number
  print(f"Binary vale of 5 : {bin(5)}")

  # binary to integer number
  print(f"Integer value of 1010 : {int('1010',2)}")

  #Classes  -> custom type

  #Specialized Data Type present in package