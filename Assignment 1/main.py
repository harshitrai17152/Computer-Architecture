from m5.objects import *
from cache import *
import SimpleOpts
import m5

# Finalize the arguments and grab the opts so we can pass it on to our objects
(opts,args)=SimpleOpts.parse_args()

## Creating the CPU
system=System()
system.clk_domain=SrcClockDomain()
system.clk_domain.clock='1GHz'
system.clk_domain.voltage_domain=VoltageDomain()

## Simple CPU with default settings
system.mem_mode='timing'
system.mem_ranges=[AddrRange('512MB')]
system.cpu=TimingSimpleCPU()

## Creating L1_Instruction_Cache and L1_Data_Cache
system.cpu.icache=L1_Instruction_Cache(opts)
system.cpu.dcache=L1_Data_Cache(opts)

## Connecting L1_Instruction_Cache 
## and L1_Data_Cache to the CPU
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

## Creating a L2 bus and connecting 
## L1_Instruction_Cache and L1_Data_Cache to it
system.l2bus=L2XBar()
system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

## Creating L2 cache and connecting it to the L2 bus
system.l2cache=L2_Cache(opts)
system.l2cache.connectCPUSideBus(system.l2bus)

## Creating a memory bus
system.membus=SystemXBar()

## Connecting L2 cache to the memory bus
system.l2cache.connectMemSideBus(system.membus)

# create the interrupt controller for the CPU
system.cpu.createInterruptController()

# For x86 only, make sure the interrupts are connected to the memory
if m5.defines.buildEnv['TARGET_ISA'] == "x86":
    system.cpu.interrupts[0].pio = system.membus.master
    system.cpu.interrupts[0].int_master = system.membus.slave
    system.cpu.interrupts[0].int_slave = system.membus.master

# Connect the system up to the membus
system.system_port=system.membus.slave

# Creating a DDR3 memory controller
system.mem_ctrl=DDR3_1600_8x8()
system.mem_ctrl.range=system.mem_ranges[0]
system.mem_ctrl.port=system.membus.master


#Running the program
process=Process()
process.cmd=['tests/test-progs/MiBench/automotive/susan/susan','tests/test-progs/MiBench/automotive/susan/input_small.pgm','tests/test-progs/MiBench/automotive/susan/output_small.smoothing.pgm','-s']
system.cpu.workload=process
system.cpu.createThreads()
root=Root(full_system=False,system=system)
m5.instantiate()
print("Beginning simulation!")
exit_event=m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))
