from big_sleep import Imagine
dream = Imagine(
    text="freedom",
    lr=5e-2,
    save_every=50,
    save_progress=True,
    image_size=256,
    seed=1471,
)
dream()