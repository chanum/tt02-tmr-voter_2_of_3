import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

@cocotb.test()
async def test_voter(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 10, units="us")
    cocotb.fork(clock.start())
    
    dut._log.info("reset")
    dut.rst.value = 1
    await ClockCycles(dut.clk, 10)
    dut.rst.value = 0

    dut._log.info("check 1 - No error")
    dut.a_in.value = 1
    dut.b_in.value = 1
    dut.c_in.value = 1
    await ClockCycles(dut.clk, 5)
    assert int(dut.v_out.value) == 1
    assert int(dut.v_error_out.value) == 0

    dut._log.info("check 2 - No error")
    dut.a_in.value = 0
    dut.b_in.value = 0
    dut.c_in.value = 0
    await ClockCycles(dut.clk, 100)
    assert int(dut.v_out.value) == 0
    assert int(dut.v_error_out.value) == 0

    dut._log.info("check 3 - error")
    dut.a_in.value = 1
    dut.b_in.value = 1
    dut.c_in.value = 0
    await ClockCycles(dut.clk, 100)
    assert int(dut.v_out.value) == 1
    assert int(dut.v_error_out.value) == 1

    dut._log.info("check 4 - error")
    dut.a_in.value = 1
    dut.b_in.value = 0
    dut.c_in.value = 1
    await ClockCycles(dut.clk, 100)
    assert int(dut.v_out.value) == 1
    assert int(dut.v_error_out.value) == 1

    dut._log.info("check 4 - error")
    dut.a_in.value = 0
    dut.b_in.value = 1
    dut.c_in.value = 1
    await ClockCycles(dut.clk, 100)
    assert int(dut.v_out.value) == 1
    assert int(dut.v_error_out.value) == 1

