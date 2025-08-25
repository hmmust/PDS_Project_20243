import multiprocessing
import time
def calc_sum(n):
    total = 0
    for i in range(0,n+1):
        total += i
        time.sleep(1)
        print(n,i)
    return total

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=2)
    result1= pool.apply(calc_sum,args=(10,)) #sequential
    result2= pool.apply(calc_sum,args=(15,)) #sequential
    pool.close()
    pool.join()  
    print("calculation Done!",result1,result2)
