# Assignment 18: Autosave EC2 Instance State Before Shutdown

## Objective
Automatically save EC2 instance data before shutdown using Lambda and EventBridge.

---

## Services Used
- AWS Lambda
- Amazon EC2
- Amazon EventBridge
- Amazon CloudWatch
- Amazon S3

---

## Architecture
EventBridge detects EC2 shutdown → triggers Lambda → Lambda creates snapshot

---

## Steps

1. Created Lambda function using Python (Boto3)
2. Configured IAM Role with EC2 permissions
3. Created EventBridge rule for EC2 state change
4. Set target as Lambda function
5. Tested by stopping EC2 instance
6. Snapshot created successfully

---

## Screenshots

### Event Trigger
![Event](screenshots/test-event1.png)

### Lambda Function
![Lambda](screenshots/lambda-function1.png)

### IAM Role
![IAM](screenshots/IAM-role1.png)

### EventBridge Rule
![Rule](screenshots/EventBridge-Rule.png)

### Snapshot Created
![Snapshot](screenshots/snapshot-test.png)

### S3 Bucket
![S3](screenshots/S3-bucket.png)

### CloudWatch Logs
![Logs](screenshots/Cloud-watch-check.png)

---

## Output
EC2 instance data is automatically backed up before shutdown using snapshots.
