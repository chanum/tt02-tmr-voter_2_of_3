`default_nettype none
`timescale 1ns/1ps

/*
this testbench just instantiates the module and makes some convenient wires
that can be driven / tested by the cocotb test.py
*/

module tb (
    // testbench is controlled by test.py
    input clk,
    input rst,
    input a_in,
    input b_in,
    input c_in,
    output v_out,
    output v_error_out
   );

    // this part dumps the trace to a vcd file that can be viewed with GTKWave
    initial begin
        $dumpfile ("tb.vcd");
        $dumpvars (0, tb);
        #1;
    end

    // wire up the inputs and outputs
    wire [7:0] inputs = {3'b0, c_in, b_in, a_in, rst, clk};
    wire [7:0] outputs;
    assign v_out = outputs[0];
    assign v_error_out = outputs[1];

    // instantiate the DUT
    voter_2_of_3 voter(
        .io_in  (inputs),
        .io_out (outputs)
        );

endmodule
