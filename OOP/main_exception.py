
import Lesson_exception1 as lesson_exception
import expection_class

try:
    lesson_exception.main()
#     если писать "as ex", то "ex" это будет объект класса, а если без него
#     except lesson_exception.EmailAlreadyExistsException:  -- это класс(!), а не объект(!)
except expection_class.EmailAlreadyExistsException as ex:
    with open('logs.txt','a+') as fl:
        fl.write(f"{ex.date} | "
                 f"{ex.traceback}" +'\n' )
except Exception:
    pass
else :
    pass

