Everything in this markdown is copy pasted from the tutorial of the community version of manim

# Creating a custom animation
Even though Manim has many built-in animations, you will find times when you need to smoothly animate from one state of a Mobject to another. If you find yourself in that situation, then you can define your own custom animation. You start by extending the Animation class and overriding its interpolate_mobject(). The interpolate_mobject() method receives alpha as a parameter that starts at 0 and changes throughout the animation. So, you just have to manipulate self.mobject inside Animation according to the alpha value in its interpolate_mobject method. Then you get all the benefits of Animation such as playing it for different run times or using different rate functions.

Let’s say you start with a number and want to create a Transform animation that transforms it to a target number. You can do it using FadeTransform, which will fade out the starting number and fade in the target number. But when we think about transforming a number from one to another, an intuitive way of doing it is by incrementing or decrementing it smoothly. Manim has a feature that allows you to customize this behavior by defining your own custom animation.

You can start by creating your own Count class that extends Animation. The class can have a constructor with three arguments, a DecimalNumber Mobject, start, and end. The constructor will pass the DecimalNumber Mobject to the super constructor (in this case, the Animation constructor) and will set start and end.

The only thing that you need to do is to define how you want it to look at every step of the animation. Manim provides you with the alpha value in the interpolate_mobject() method based on frame rate of video, rate function, and run time of animation played. The alpha parameter holds a value between 0 and 1 representing the step of the currently playing animation. For example, 0 means the beginning of the animation, 0.5 means halfway through the animation, and 1 means the end of the animation.

In the case of the Count animation, you just have to figure out a way to determine the number to display at the given alpha value and then set that value in the interpolate_mobject() method of the Count animation. Suppose you are starting at 50 and incrementing until the DecimalNumber reaches 100 at the end of the animation.

If alpha is 0, you want the value to be 50.

If alpha is 0.5, you want the value to be 75.

If alpha is 1, you want the value to be 100.

Generally, you start with the starting number and add only some part of the value to be increment according to the alpha value. So, the logic of calculating the number to display at each step will be 50 + alpha * (100 - 50). Once you set the calculated value for the DecimalNumber, you are done.

Once you have defined your Count animation, you can play it in your Scene for any duration you want for any DecimalNumber with any rate function.


# Scenes
The Scene class is the connective tissue of manim. Every mobject has to be added to a scene to be displayed, or removed from it to cease being displayed. Every animation has to be played by a scene, and every time interval where no animation occurs is determined by a call to wait(). All of the code of your video must be contained in the construct() method of a class that derives from Scene. Finally, a single file may contain multiple Scene subclasses if multiple scenes are to be rendered at the same time.