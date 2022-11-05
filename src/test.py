import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles
import random
from voter_model import voter_model

@cocotb.test()
async def test_voter_directed(dut):
    dut._log.info("- START TEST----------------------")
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())
    
    dut._log.info("- Reset")
    dut.rst.value = 1
    await ClockCycles(dut.clk, 10)
    dut.rst.value = 0

    dut._log.info("- Check 1 ---")
    dut.a_in.value = 1
    dut.b_in.value = 1
    dut.c_in.value = 1
    await ClockCycles(dut.clk, 5)
    assert int(dut.v_out.value) == 1
    assert int(dut.v_error_out.value) == 0

    dut._log.info("- Check 2  ---")
    dut.a_in.value = 0
    dut.b_in.value = 0
    dut.c_in.value = 0
    await ClockCycles(dut.clk, 5)
    assert int(dut.v_out.value) == 0
    assert int(dut.v_error_out.value) == 0

    dut._log.info("- Check 3 ---")
    dut.a_in.value = 1
    dut.b_in.value = 1
    dut.c_in.value = 0
    await ClockCycles(dut.clk, 5)
    assert int(dut.v_out.value) == 1
    assert int(dut.v_error_out.value) == 1

    dut._log.info("- Check 4 ---")
    dut.a_in.value = 1
    dut.b_in.value = 0
    dut.c_in.value = 1
    await ClockCycles(dut.clk, 5)
    assert int(dut.v_out.value) == 1
    assert int(dut.v_error_out.value) == 1

    dut._log.info("- Check 4 ---")
    dut.a_in.value = 0
    dut.b_in.value = 1
    dut.c_in.value = 1
    await ClockCycles(dut.clk, 5)
    assert int(dut.v_out.value) == 1
    assert int(dut.v_error_out.value) == 1
    
    dut._log.info("- END TEST ----------------------")


@cocotb.test()
async def test_voter_random(dut):
    dut._log.info("- START TEST----------------------")
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())
    
    dut._log.info("- Reset")
    dut.rst.value = 1
    await ClockCycles(dut.clk, 10)
    dut.rst.value = 0
    
    await ClockCycles(dut.clk, 5)
    for i in range(50):
        dut._log.info("Random %s", i)
        A = random.getrandbits(1)
        B = random.getrandbits(1)
        C = random.getrandbits(1)
        dut._log.info("* Values A = %s", A)
        dut._log.info("* Values B = %s", B)
        dut._log.info("* Values C = %s", C)

        dut.a_in.value = A
        dut.b_in.value = B
        dut.c_in.value = C
        await ClockCycles(dut.clk, 3)
        
        V, E = voter_model(A, B, C)
        assert dut.v_out.value == V
        assert dut.v_error_out.value == E

    dut._log.info("END TEST ----------------------")
