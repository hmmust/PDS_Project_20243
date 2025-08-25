import multiprocessing
import time
def calc_sum(n):
    total = 0
    for i in range(0,n+1):
        total += i
        time.sleep(1)
        print(n,i)
    print("result = ",total)

print(multiprocessing.cpu_count())

if __name__ == "__main__":
    worker1= multiprocessing.Process(target=calc_sum,args=(10,))
    worker2= multiprocessing.Process(target=calc_sum,args=(15,))
    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()
    print("calculation Done!")
