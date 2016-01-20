Digilent FPGA: Basys 3 Artix-7 FPGA Trainer Board
#################################################

:Date: 2016-01-17
:Category: HDL
:Tags: FPGA, CPU, MyHDL

Modern processors are deigned with Hardware Description Languages, not by
engineers drawing old-fashioned electronic circuit diagrams. So, students
wishing to explore how those modern processors are actually designed need an
environment where they can explore the architecture concepts, and software tools
used to design the chips they end up using.

The foundation component of the modern microprocessor is the NAND gate. It can be proven that if you have enough NAND gates around, you can build just about any digital circuit, and that fact has spawned a new kind of component: The Field Programmable Gate Array, or FPGA.

Basically, an FPGA is just that, an array of NAND gates that can be
electrically interconnected using software to produce a digital curcuit.
Typical FPGA devices might have 500,000 NAND gates in one chip. That means we
can set up pretty sophisticated circuits easily. Since FPGA boards are
controlled by software, we can design, construct, and verify the correctness of
a digital circuit easily. Once we are happy with the design, additional tools
can be added to our development set that can be sent to manufacturing
facilities to build the actual physical hardware.  We have reached the point
where designing hardware is done using software! 

Getting your Hands on a FPGA 
****************************

In this series of articles, I am going to develop a simple microprocessor using
a Python based hardware description languag. The tool I will use if MyHDL. Once
we have designed the processor, we will generate data files that will be used
to program a specific FPGA board: The Digilend Basys 3 Artiz-7 board:

..  image:: images/Basys3Artix7.png
    :align: center
    :alt: Basys 3 Artix-7 FPGA


