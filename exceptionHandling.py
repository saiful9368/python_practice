#try:
    #this block of code willl run and throw errors if occurs
#except:
    #this will raise the orrors

#else:
    #this will excute if there are no errors
#finally:
    #this will excute regardless the result of try and except

# try:
#     f=open("demo.py")
#     try:
#         f.write("abc")
#     except:
#         print("Error in file")
#     finally:
#         f.close()
# except:
#     print("can't open the file")

a=5
if a<10:
    raise Exception("Value is less than 5")