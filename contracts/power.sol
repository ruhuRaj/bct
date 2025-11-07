// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract power {
  
  uint voltage;
  uint current;
  
  uint role;
  constructor() public{
    voltage=0;
    current=0;
  }

  function addPower(uint v, uint c) public {
    voltage+=v;
    current+=c;
  }

  function viewPower() public view returns (uint) {
    return (voltage*current);
  }

  function checkPower() public returns(uint) {
    uint p;
    p=voltage*current;
    if(p>0 && p<10000) {
      role=0;
    } else if(p>10000) {
      role=1;
    }
    return (role);
  }
  
}
