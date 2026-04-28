from celery import shared_task


@shared_task
def send_application_notification(recruiter_email, candidate_name, job_title):
    """
    Celery task — Email notification jab candidate apply kare.
    CELERY_TASK_ALWAYS_EAGER = True hone ki wajah se ye seedha chalega.
    Production mein ye background mein jayega.
    """
    print(f"Email sent to {recruiter_email}: {candidate_name} applied for {job_title}")
    return f"Notification sent successfully!"


@shared_task
def send_status_update(candidate_email, job_title, new_status):
    """
    Celery task — Status update hone pe candidate ko email.
    """
    print(f"Email sent to {candidate_email}: Your application for {job_title} is now {new_status}")
    return f"Status update sent!"