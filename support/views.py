from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json

from .models import Conversation, Message
from .forms import MessageForm

class LandingView(View):
    def get(self, request):
        return render(request, 'support/landing.html')

class ChatView(View):
    def get(self, request):
        # Retrieve the latest conversation or create a new one
        # For a real app, this should be tied to request.user or session
        conversation = Conversation.objects.order_by('-updated_at').first()
        if not conversation:
            conversation = Conversation.objects.create()

        messages = conversation.messages.all()
        form = MessageForm()

        return render(request, 'support/chat.html', {
            'conversation': conversation,
            'messages': messages,
            'form': form,
        })

class MessageAPIView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            content = data.get('message', '').strip()
            
            if not content:
                return JsonResponse({'error': 'Message content is required'}, status=400)

            # Get the ongoing conversation
            conversation = Conversation.objects.order_by('-updated_at').first()
            if not conversation:
                conversation = Conversation.objects.create()

            # Save the user's message
            user_message = Message.objects.create(
                conversation=conversation,
                sender='user',
                content=content
            )

            # Update conversation timestamp
            conversation.save()

            # Generate mocked AI response
            # FUTURE EXTENSION: Call OpenAI API or other NLP service here
            ai_content = f"Mocked AI: I received your message '{content}'. I am ready to be integrated with a real AI!"
            
            # Save the AI response
            ai_message = Message.objects.create(
                conversation=conversation,
                sender='ai',
                content=ai_content
            )

            # Update conversation timestamp again
            conversation.save()

            return JsonResponse({
                'success': True,
                'user_message': {
                    'sender': 'user',
                    'content': user_message.content,
                    'timestamp': user_message.timestamp.strftime('%I:%M %p')
                },
                'ai_message': {
                    'sender': 'ai',
                    'content': ai_message.content,
                    'timestamp': ai_message.timestamp.strftime('%I:%M %p')
                }
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
