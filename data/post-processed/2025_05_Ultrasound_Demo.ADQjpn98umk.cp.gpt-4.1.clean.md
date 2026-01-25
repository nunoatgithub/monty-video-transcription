I'll show around the setup while Will and Niels get everything ready. Here's our Windows laptop that communicates with the vibe trackers. The vibe trackers are set up down here—there's one here, and another one over there. This is just strapping the tracker to the ultrasound device. This indicates it's on, and it's connected to the iPad over here. The setup was sufficiently complex that we ended up creating a surgical checklist to go through every time to make sure everything is running well.

Terry, do you have an object you'd like us to test on? Let's do the hot sauce because it has a different shape.

How empty is the sauce? Hot sauce, Niels—no comment. Right now, you can see the probe. Sometimes it gets a bit laggy when we're on Zoom because there are too many devices running, but you can see the probe moving relative to the setup. Maybe if you switch over, Will, to the other view. On the top left, you see the full ultrasound image, and next to it, the extracted patch and the features we extracted. To the side of that, you see the relative locations in the world that it estimated.

On the bottom row, you can see Monty's current hypothesis of what it thinks it is sensing. Almost all of the objects are still possible. The most likely hypothesis right now is Monty's heart. What did we actually put in to change that? The hot sauce. Hot sauce. Okay, a goal state. Gold state—huge. Not yet. Sorry, the ultrasound just needs a lot of jelly and fluid to work; any air and it doesn't say anything. We're not a hundred percent sure yet that all of the coordinate transforms are correct. There might be some room for improvement. It probably is the case that the coordinate transforms aren't totally right because this should be doable for Monty. We just need a few more observations. Did we show the goal? Here we go, here's a good goal state. Right now, the probe is over here and the goal state is on the other side. So the user actually moves the probe.

But the problem is we lost one of the trackers, unfortunately. That's pretty close. Maybe if you rotate it, Will, so I can see. Once it goes into the actual point, the arrow disappears. You see that once the arrow disappears, if you keep doing inference and get another goal state, it will do the same thing—it'll create a new arrow and try to be a bit quicker.

You can see on the ultrasound image at the top these zebra stripes; that's just one of the artifacts that comes in.

Are those reflections or something? There we go. We finished. It's like bouncing back and forth and creating a false image at a certain depth. So what did it categorize?

Monty's heart. Monty's thought. Oh, that's a shame.