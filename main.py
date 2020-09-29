import quopri as qp
import io

def encodestring(instring, tabs=0):
    outfile = io.BytesIO()
    qp.encode(io.BytesIO(instring.encode()), outfile, tabs)
    return outfile.getvalue().decode()
    
def decodestring(instring):
    outfile = io.BytesIO()
    qp.decode(io.BytesIO(instring.encode()), outfile)
    return outfile.getvalue().decode()
    
def body(name, tel):
    return f"""BEGIN:VCARD
VERSION:2.1
N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;{name};;;
FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:{name}
TEL;CELL:{tel}
END:VCARD"""
	
	
if __name__ == "__main__":
    import pandas as pd
    
    data = pd.read_csv(r"vcf.csv")
    
    data['qp'] = data['name'].apply(encodestring)
    
    for i in range(data.shape[0]):
        b = body(data.iloc[i,3], data.iloc[i,1])
        print(b)
        
