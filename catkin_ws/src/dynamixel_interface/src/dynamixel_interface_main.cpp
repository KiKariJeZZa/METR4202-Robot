/// @file    dynamixel_interface_main.cpp
/// @brief   entry point for the ros dynamixel interface
///
/// @author  Tom Molnar (tom.molnar@data61.csiro.au)
/// @date    November 2020
/// @version 0.0.1
///
/// CSIRO Autonomous Systems Laboratory
/// Queensland Centre for Advanced Technologies
/// PO Box 883, Kenmore, QLD 4069, Australia
///
/// (c) Copyright CSIRO 2020
///
/// CSIRO Open Source Software License Agreement (variation of the BSD / MIT License)
/// Copyright (c) 2020, Commonwealth Scientific and Industrial Research Organisation (CSIRO) ABN 41 687 119 230.
/// All rights reserved. CSIRO is willing to grant you a license to the dynamixel_actuator ROS packages on the following
/// terms, except where otherwise indicated for third party material. Redistribution and use of this software in source
/// and binary forms, with or without modification, are permitted provided that the following conditions are met:
/// - Redistributions of source code must retain the above copyright notice, this list of conditions and the following
///   disclaimer.
/// - Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
///   disclaimer in the documentation and/or other materials provided with the distribution.
/// - Neither the name of CSIRO nor the names of its contributors may be used to endorse or promote products derived from
///   this software without specific prior written permission of CSIRO.
///
/// EXCEPT AS EXPRESSLY STATED IN THIS AGREEMENT AND TO THE FULL EXTENT PERMITTED BY APPLICABLE LAW, THE SOFTWARE IS
/// PROVIDED "AS-IS". CSIRO MAKES NO REPRESENTATIONS, WARRANTIES OR CONDITIONS OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
/// BUT NOT LIMITED TO ANY REPRESENTATIONS, WARRANTIES OR CONDITIONS REGARDING THE CONTENTS OR ACCURACY OF THE SOFTWARE,
/// OR OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, THE ABSENCE OF LATENT OR OTHER
/// DEFECTS, OR THE PRESENCE OR ABSENCE OF ERRORS, WHETHER OR NOT DISCOVERABLE.
/// TO THE FULL EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT SHALL CSIRO BE LIABLE ON ANY LEGAL THEORY (INCLUDING,
/// WITHOUT LIMITATION, IN AN ACTION FOR BREACH OF CONTRACT, NEGLIGENCE OR OTHERWISE) FOR ANY CLAIM, LOSS, DAMAGES OR
/// OTHER LIABILITY HOWSOEVER INCURRED.  WITHOUT LIMITING THE SCOPE OF THE PREVIOUS SENTENCE THE EXCLUSION OF LIABILITY
/// SHALL INCLUDE: LOSS OF PRODUCTION OR OPERATION TIME, LOSS, DAMAGE OR CORRUPTION OF DATA OR RECORDS; OR LOSS OF
/// ANTICIPATED SAVINGS, OPPORTUNITY, REVENUE, PROFIT OR GOODWILL, OR OTHER ECONOMIC LOSS; OR ANY SPECIAL, INCIDENTAL,
/// INDIRECT, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES, ARISING OUT OF OR IN CONNECTION WITH THIS AGREEMENT, ACCESS
/// OF THE SOFTWARE OR ANY OTHER DEALINGS WITH THE SOFTWARE, EVEN IF CSIRO HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
/// CLAIM, LOSS, DAMAGES OR OTHER LIABILITY. APPLICABLE LEGISLATION SUCH AS THE AUSTRALIAN CONSUMER LAW MAY APPLY
/// REPRESENTATIONS, WARRANTIES, OR CONDITIONS, OR IMPOSES OBLIGATIONS OR LIABILITY ON CSIRO THAT CANNOT BE EXCLUDED,
/// RESTRICTED OR MODIFIED TO THE FULL EXTENT SET OUT IN THE EXPRESS TERMS OF THIS CLAUSE ABOVE "CONSUMER GUARANTEES".
/// TO THE EXTENT THAT SUCH CONSUMER GUARANTEES CONTINUE TO APPLY, THEN TO THE FULL EXTENT PERMITTED BY THE APPLICABLE
/// LEGISLATION, THE LIABILITY OF CSIRO UNDER THE RELEVANT CONSUMER GUARANTEE IS LIMITED (WHERE PERMITTED AT CSIRO'S
/// OPTION) TO ONE OF FOLLOWING REMEDIES OR SUBSTANTIALLY EQUIVALENT REMEDIES:
/// (a)  THE REPLACEMENT OF THE SOFTWARE, THE SUPPLY OF EQUIVALENT SOFTWARE, OR SUPPLYING RELEVANT SERVICES AGAIN;
/// (b)  THE REPAIR OF THE SOFTWARE;
/// (c)  THE PAYMENT OF THE COST OF REPLACING THE SOFTWARE, OF ACQUIRING EQUIVALENT SOFTWARE, HAVING THE RELEVANT
///      SERVICES SUPPLIED AGAIN, OR HAVING THE SOFTWARE REPAIRED.
/// IN THIS CLAUSE, CSIRO INCLUDES ANY THIRD PARTY AUTHOR OR OWNER OF ANY PART OF THE SOFTWARE OR MATERIAL DISTRIBUTED
/// WITH IT.  CSIRO MAY ENFORCE ANY RIGHTS ON BEHALF OF THE RELEVANT THIRD PARTY.

#include <dynamixel_interface/dynamixel_interface_controller.h>
#include <ros/ros.h>

/// main
int main(int argc, char **argv)
{
  // ros initialise
  ros::init(argc, argv, "dynamixel_interface_node");

  // create controller
  dynamixel_interface::DynamixelInterfaceController controller;

  // parse params
  if (!controller.parseParameters())
  {
    return 1;
  }

  // intialise
  if (!controller.initialise())
  {
    return 2;
  }

  // initialise rate controller
  ros::Rate rate(controller.getLoopRate());

  // Loop and process
  while (ros::ok())
  {
    controller.loop();

    ros::spinOnce();
    rate.sleep();
  }

  return 0;
}
