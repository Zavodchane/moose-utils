import albumentations as A

transform_1 = A.Compose([A.HorizontalFlip(p=1.0)])
transform_2 = A.Compose([
    A.HorizontalFlip(p=1.0),
    A.Rotate(limit=(10, 10), p=1.0),
])
transform_3 = A.Compose([
    A.HorizontalFlip(p=1.0),
    A.Rotate(limit=(10, 10), p=1.0),
    A.RandomBrightnessContrast(brightness_limit=(0.2, 0.3), contrast_limit=0, p=1.0)
])
transform_4 = A.Compose([
    A.Rotate(limit=(10, 10), p=1.0),
    A.RandomBrightnessContrast(brightness_limit=(0.2, 0.3), contrast_limit=0, p=1.0)
])
