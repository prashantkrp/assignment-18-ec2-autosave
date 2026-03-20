## Assignment 18: Autosave EC2 Instance State Before Shutdown

### Objective

To automatically save the state of an EC2 instance before it is terminated using AWS services.

---

### Services Used

* Amazon EC2
* AWS Lambda
* Amazon EventBridge (CloudWatch Events)
* Amazon S3 (optional)
* Amazon CloudWatch

---

### Implementation Steps

1. Created an S3 bucket for storing backups (optional).
2. Created an IAM role with required permissions (EC2, S3, CloudWatch).
3. Developed a Lambda function using Boto3 to:

   * Detect EC2 instance ID
   * Create EBS snapshots of attached volumes
4. Created an EventBridge rule to detect EC2 state change:

   * Event type: EC2 Instance State-change Notification
   * State: shutting-down
5. Connected the EventBridge rule to trigger the Lambda function.
6. Tested by terminating an EC2 instance.

---

### Output

* EBS snapshots were automatically created before instance termination.
* Logs were successfully generated in CloudWatch.

---

### Conclusion

This setup ensures automatic backup of EC2 instances before termination, preventing data loss and improving system reliability.

---

### Real-World Use Case

Used in production environments to safeguard critical data before shutting down or terminating EC2 instances.

