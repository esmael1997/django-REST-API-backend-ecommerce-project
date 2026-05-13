# Password Reset System Design

## Flow
1. User submits email
2. System checks rate limit (IP + email)
3. Celery sends async email
4. Email contains tokenized reset link
5. Token validated on reset confirm view
6. Password updated using SetPasswordForm

## Security Features
- 48h token validity
- Rate limiting (60s)
- Django secure token generator
- No direct password exposure

## Async Strategy
- Celery used for email dispatch
- Prevents blocking request thread

## AI/Resources
- Django official docs (auth.tokens)
- Celery official docs
- OpenAI assisted architecture design