import unittest
from EmotionDetection import emotion_detection

emotion_detector = emotion_detection.emotion_detector

class TestDominantEmotion(unittest.TestCase):
    def test_joy(self):
        text = "I am glad this happened."
        emotion_score = emotion_detector(text)
        self.assertEqual(emotion_score["dominant_emotion"], "joy")
    
    def test_anger(self):
        text = "I am really mad about this."
        emotion_score = emotion_detector(text)
        self.assertEqual(emotion_score["dominant_emotion"], "anger")

    def test_disgust(self):
        text = "I feel disgusted just hearing about this."
        emotion_score = emotion_detector(text)
        self.assertEqual(emotion_score["dominant_emotion"], "disgust")
    
    def test_sadness(self):
        text = "I am so sad about this."
        emotion_score = emotion_detector(text)
        self.assertEqual(emotion_score["dominant_emotion"], "sadness")

    def test_fear(self):
        text = "I am really afraid that this will happen."
        emotion_score = emotion_detector(text)
        self.assertEqual(emotion_score["dominant_emotion"], "fear")

