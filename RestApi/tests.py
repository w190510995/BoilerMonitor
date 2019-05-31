from django.test import TestCase

# Create your tests here.

if __name__ == '__main__':
    FixedValueFunctions ={ #固定定值

        'LowerWaterWall':111111111,
        'UpperWaterWall1':22222222222,

    }

    for key,value in FixedValueFunctions.items():
        print(key,value)
