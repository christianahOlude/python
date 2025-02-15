import unittest

from diary import diary
from diary.diary import Diary


class DiaryTest(unittest.TestCase):

    def setUp(self):
        self.diary = Diary()

    def test_that_diary_is_not_locked_by_default(self):
        self.diary.isLocked = False
        self.assertFalse(self.diary.isLocked)

    def test_that_diary_can_be_added(self):
        self.diary.create_entry("title","content")
        self.assertEqual(1 ,self.diary.create_entry("title","content"))

    def test_that_diary_can_be_deleted(self):
        self.diary.create_entry("title","content")
        self.assertEqual(1 ,self.diary.create_entry("title","content"))
        self.diary.delete_entry(1)
        self.assertEqual(None,self.diary.delete_entry(0))

    def test_that_diary_can_be_updated(self):
        self.diary.create_entry("title","content")
        self.assertEqual(1 ,self.diary.create_entry("title","content"))
        self.diary.update_diary(1,"content","title")
        self.assertEqual(1 ,self.diary.create_entry("title","content"))

