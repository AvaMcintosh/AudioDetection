import bitstring
from bitstring import BitArray

base = BitArray(bytes=open('src/NoiseWithHonk.wav', 'rb').read())
##print(base.bin)

carHonk = BitArray(bytes=open('src/CarHonk1.wav', 'rb').read())

chunk_size = 100000

for i in range(0, len(base), chunk_size):
    # Get the chunk from index i to i + chunk_size
    chunk = base[i:i + chunk_size]
    
    #print(f"Processing chunk starting at index {i}: {chunk}")

    if(chunk.bin in carHonk.bin):{
        print("HONK")
    }
    else: {
        print("Nothing")
    }

    # Process the chunk
    

##test = base[:20]

##print(base.bin)


## take in input
## every (Number of bits) check for comparison to car honking bitwise

## if there is over a 90% match say true


#carHonk = BitArray(bytes=open('src/CarHonk1.wav', 'rb').read())
##print(carHonk.bin)