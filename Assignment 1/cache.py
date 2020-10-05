from m5.objects import Cache
import SimpleOpts
import m5

class L1_Cache(Cache):
	assoc=2
	data_latency=2
	tag_latency=2
    	response_latency=2
    	
    	mshrs=4
      	tgts_per_mshr=20
      	
      	def __init__(self,options=None):
        	super(L1_Cache,self).__init__()
        	pass
      	
      	def connectCPU(self,cpu):
		raise NotImplementedError
    
	def connectBus(self,bus):
    		self.mem_side=bus.slave

class L2_Cache(Cache):
   	size='256kB'
    	assoc=4
	tag_latency=10
    	data_latency=10
    	response_latency=10
   
    	mshrs=20
    	tgts_per_mshr=12     
    	
    	SimpleOpts.add_option('--l2_size',help="L2 cache size. Default: %s" % size)
  	SimpleOpts.add_option('--l2_associativity',help="L2 associativity. Default: %d" % assoc)

	def __init__(self,opts=None):
        	super(L2_Cache,self).__init__()   	
        	
        	if not opts:
        		return    
        	if opts.l2_size:
        		self.size=opts.l2_size
        	if opts.l2_associativity:
        		self.assoc=opts.l2_associativity    	
        	
        	print("L2 Cache Size (kB): %d" %self.size)
    		print("L2 Cache Associativity: %d" %self.assoc)
        		
	def connectCPUSideBus(self,bus):
		self.cpu_side=bus.master
		
	def connectMemSideBus(self,bus):
		self.mem_side=bus.slave 
		      	
class L1_Instruction_Cache(L1_Cache):
   	size='16kB'
   	
   	SimpleOpts.add_option('--l1i_size',help="L1 instruction cache size. Default: %s" % size)

    	def __init__(self,opts=None):
        	super(L1_Instruction_Cache, self).__init__(opts)
        	if not opts or not opts.l1i_size:
	            	return
        	self.size=opts.l1i_size
   	
   	def connectCPU(self,cpu):
	   	self.cpu_side=cpu.icache_port

class L1_Data_Cache(L1_Cache):
   	size='16kB'
   	
   	SimpleOpts.add_option('--l1d_size',help="L1 data cache size. Default: %s" % size)

    	def __init__(self,opts=None):
        	super(L1_Data_Cache, self).__init__(opts)
        	if not opts or not opts.l1d_size:
            		return
        	self.size=opts.l1d_size
        	
  	def connectCPU(self,cpu):
		self.cpu_side=cpu.dcache_port
		
