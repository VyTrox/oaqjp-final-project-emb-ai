from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        joy = emotion_detector('I am glad this happened')
        self.assertEqual(joy, 'joy')
        
        anger = emotion_detector('I am really mad about this')
        self.assertEqual(anger, 'anger')
        
        disgust = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(disgust, 'disgust')

        sadness = emotion_detector('I am so sad about this')
        self.assertEqual(sadness, 'sadness')

        fear = emotion_detector('I am really afraid that this will happen	')
        self.assertEqual(fear, 'fear')

unittest.main()
