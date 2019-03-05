# DBCheckStatus

[![GitHub Stars](https://img.shields.io/github/stars/mhorger3/DBCheckStatus.svg)](https://github.com/mhorger3/DBCheckStatus/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/mhorger3/DBCheckStatus.svg)](https://github.com/mhorger3/DBCheckStatus/issues) [![Current Version](https://img.shields.io/badge/version-1.0.1-green.svg)](https://github.com/mhorger3/DBCheckStatus)


This project is two functions, one a base function and the other with SMS capabilities, to check if my Amazon AWS RDS Database Instances are up. Instead of having to navigate to https://console.aws.amazon.com/rds/home?region=us-east-1 to see the status, this sends a simple text!

---

## Setup

In order to get this code working with your AWS RDS Instances, you'll have to configure your target endpoints and VPC Security Group so that the Lambda Functions can actually reach the endpoints. You can navigate to https://console.aws.amazon.com/vpc/home?region=us-east-1 in order to see your created Virtual Private Clouds.

---

## Usage

These functions have two use triggers that I can think of. The first is a simple Lambda invocation, which could be trigger via a scheduled CloudWatch cron expression `0/60 11-4 * * ? *`, which I am using for the default job, or even an IOT button (which I have setup at my desk and if you are interested, here's the button I have https://www.amazon.com/1st-Generation-AWS-IoT-Button/dp/B01C7WE5WM). The second is via E-mail / SMS triggers. I don't have these setup where I can trigger it via a remote SMS, but it can send out the status via SMS / E-mail. 
