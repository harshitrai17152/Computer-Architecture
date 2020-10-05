import matplotlib.pyplot as plt

c_32=[0.554067,0.543287,0.536753,0.534793]
c_64=[0.521072,0.515844,0.512578,0.508004]
c_256=[0.497877,0.49461,0.49461,0.49461]
c_1024=[0.49461,0.49461,0.49461,0.49461]
associativity=[2,4,8,16]

lin=[32,64,256,1024]
plt.plot(lin,c_32,'r',marker='o')
plt.plot(lin,c_64,'b',marker='o')
plt.plot(lin,c_256,'g',marker='o')
plt.plot(lin,c_1024,'c',marker='o')

for i in range(4):
    txt="Assoc: "+str(associativity[i])
    plt.annotate(txt,(lin[i],c_32[i]))
    plt.annotate(txt,(lin[i],c_64[i]))
    plt.annotate(txt,(lin[i],c_256[i]))
    plt.annotate(txt,(lin[i],c_1024[i]))
    
plt.gca().legend(('32 kB','64 kB','256 kB','1024 kB'))
plt.xlabel('Cache Size (kB)')
plt.ylabel('L2 Overall Miss Rate')
plt.title('L2 Cache Miss Rate for different sizes and associativity')
plt.show()
