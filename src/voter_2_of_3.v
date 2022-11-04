

`default_nettype none

module voter_2_of_3 (
  input [7:0] io_in,
  output [7:0] io_out
);
  wire clock = io_in[0];
  wire reset = io_in[1];
  wire a_in = io_in[2];
  wire b_in = io_in[3];
  wire c_in = io_in[4];
  
  wire nand1; 
  wire nand2; 
  wire nand3; 

  reg a_r;
  reg b_r;
  reg c_r;
  reg voter_r;
  reg voter_error_r;

  // Register inputs
  always@(posedge clock) begin
    if (reset) begin
      a_r <= 1'b0;
      b_r <= 1'b0; 
      c_r <= 1'b0; 
    end else begin
      a_r <= a_in;
      b_r <= b_in; 
      c_r <= c_in; 
    end
  end

  // Error generator
  always@(a_r, b_r, c_r) begin
    if (a_r == b_r && b_r == c_r) begin
      voter_error_r = 1'b0;
    end else begin
      voter_error_r = 1'b1;
    end
  end

  assign io_out[0] = voter_error_r;

  // Voter 2 of 3
  assign nand1 = ~(a_r & b_r);
  assign nand2 = ~(b_r & c_r);
  assign nand3 = ~(a_r & c_r);

  assign io_out[1] = ~(nand1 & nand2 & nand3);

  // free io
  // io_in[5]
  // io_in[6]
  // io_in[7]
  // io_out[2]
  // io_out[3]
  // io_out[4]
  // io_out[5]
  // io_out[6]

endmodule