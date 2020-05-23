from django.test import TestCase
from Book_App.models import Seat
from Book_App.models import Reservation
from Account_App.models import UserProf
from django.contrib.auth.models import User


# Seat类测试
class SeatTestCase(TestCase):
    def setUp(self):
        Seat.objects.create(is_quiet_area=True, floor=1, area='A', table_type=4, has_power=False, \
                            table_position_noisy='', table_position_quiet='A100-001')

    def test_Seat_models(self):
        result = Seat.objects.get(table_position_quiet='A100-001')
        self.assertEqual(result.table_position_quiet, 'A100-001')
        self.assertEqual(result.is_quiet_area, True)
        self.assertEqual(result.floor, 1)
        self.assertEqual(result.area, 'A')
        self.assertEqual(result.table_type, 4)
        self.assertEqual(result.has_power, False)
        self.assertEqual(result.table_position_noisy, '')
        self.assertEqual(result.table_position_quiet, 'A100-001')


# Reservation类测试
class ReservationTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(username='Test_User')
        test_user = UserProf.objects.create(user=test_user, icon='static/image/zhangzhe.jpg',
                                            credit=5, delete_times=0, introduction='无', name='Test_User',
                                            student_number='000001', phone_number='000001')
        test_seat = Seat.objects.create(is_quiet_area=True, floor=1, area='A', table_type=4, has_power=False,
                                        table_position_noisy='', table_position_quiet='A100-001')
        Reservation.objects.create(account=test_user, seat=test_seat, is_delete=True, date="2020-5-20", time_id=1)

    def test_Reservation_models(self):
        pass
        test_user = UserProf.objects.get(name='Test_User')
        test_seat = Seat.objects.get(table_position_quiet='A100-001')
        result = Reservation.objects.get(date="2020-5-20", time_id=1, account_id=test_user.id, seat_id=test_seat.id)

        self.assertEqual(result.account.name, 'Test_User')
        self.assertEqual(result.seat.area, 'A')

        self.assertEqual(result.is_delete, True)
        self.assertEqual(result.time_choice, (
            (1, "8:00-11:00"),
            (2, "13:00-17:00"),
            (3, "18:00-21:00"),
        ))
        self.assertEqual(result.time_id, 1)


if __name__ == '__main__':
    TestCase.main()
