(define (problem move_r5_to_goal) (:domain hanoiPLUS)
(:objects
	r1 r2 r3 r4 r5 w1 w2 w3 w4 w5 - disk
	rod1 rod2 rod3 - rod
	h - hand
)
(:init
	 (clear r1) (clear w1) 
	 (located r1 rod1)
	 (located w2 rod1)
	 (located r3 rod1)
	 (located w4 rod1)
	 (located r5 rod1)

	 (located w1 rod2)
	 (located r2 rod2)
	 (located w3 rod2)
	 (located r4 rod2)
	 (located w5 rod2)
 

	(=(disks_number rod1)5) (=(disks_number rod2)5) 
	(=(disks_number rod3)0) 

	(on r1 w2)(on w2 r3)(on r3 w4)(on w4 r5)
	(on w1 r2)(on r2 w3)(on w3 r4)(on r4 w5)

	(smaller r1 w2)(smaller r1 r2)(smaller r1 w3)(smaller r1 r3)(smaller r1 w4)(smaller r1 r4)(smaller r1 w5)(smaller r1 r5)
	(smaller w1 r2)(smaller w1 w2)(smaller w1 r3)(smaller w1 w3)(smaller w1 r4)(smaller w1 w4)(smaller w1 r5)(smaller w1 w5)
	(smaller r2 w3)(smaller r2 r3)(smaller r2 w4)(smaller r2 r4)(smaller r2 w5)(smaller r2 r5)
	(smaller w2 r3)(smaller w2 w3)(smaller w2 r4)(smaller w2 w4)(smaller w2 r5)(smaller w2 w5)
	(smaller r3 w4)(smaller r3 r4)(smaller r3 w5)(smaller r3 r5)
	(smaller w3 r4)(smaller w3 w4)(smaller w3 r5)(smaller w3 w5)
	(smaller r4 w5)(smaller r4 r5)
	(smaller w4 r5)(smaller w4 w5)
	
	(equal r1 w1)(equal w1 r1)
	(equal r2 w2)(equal w2 r2)
	(equal r3 w3)(equal w3 r3)
	(equal r4 w4)(equal w4 r4)
	(equal r5 w5)(equal w5 r5)
)
(:goal (and


	(located w5 rod2) (located r4 rod2) (located w4 rod2) (located w3 rod2) 
	(located r3 rod2) (located r2 rod2) (located w2 rod2) (located w1 rod2) 
	(located r1 rod2)

	(located r5 rod3) 

	(clear r5) 
	(clear r1) 

	(not(clear w1)) (not(clear w2)) (not(clear w3)) (not(clear w4)) (not(clear w5)) 
	(not(clear r2)) (not(clear r3)) (not(clear r4)) 
	
	(on r1 w1)(on w1 w2)(on w2 r2)(on r2 r3)(on r3 w3)(on w3 w4)(on w4 r4)
	(on r4 w5)
	 
	(=(disks_number rod1)0) (=(disks_number rod2)9) 
	(=(disks_number rod3)1) 
)
)
)