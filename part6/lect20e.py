import pandas as pd
import multiprocessing

def process_chuck(chunk):
        chunk.Year.fillna(2019,inplace=True)
        chunk.Major.replace({"DSS":"DS"," SE":"SE"},inplace=True)
        chunk.Year = chunk.Year.astype(int)
        return chunk
    
if __name__ == "__main__":
    students = pd.read_csv("./part3/students.csv",chunksize=3)
    chunks=[]
    pool = multiprocessing.Pool(processes=16)
    for chunk in students:
        chunk = pool.apply_async(process_chuck, args=(chunk,))
        chunks.append(chunk.get())
    pool.close()
    pool.join()
    students = pd.concat(chunks,axis=0,ignore_index=True)
    print(students)