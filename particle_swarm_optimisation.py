
# coding: utf-8

# In[6]:


#library imports
import random
import numpy as np

#initialising W,c1 and c2
W=0.5
c1=0.8
c2=0.9

#inputs
n_iterations = int(input("Inform the number of iterations: "))
target_error = float(input("Inform the target error: "))
n_particles = int(input("Inform the number of particles: "))


# In[7]:


#function that models the problem
def fitness_function(position):
    return position[0]**2 + position[1]**2 + 1


# In[8]:


#class handling the particles
class particle ():
    def __init__(self):
        self.position=np.array([(-1)**(bool(random.getrandbits(1)))*random.random()*50,(-1)**(bool(random.getrandbits(1)))*random.random()*50])
        self.pbest_position=self.position
        self.pbest_value=float('inf')
        self.velocity=np.array([0,0])
        
    def __str__(self):
        print("position=",self.position,"pbest position=",self.pbest_position)
        
    def move(self):
        self.position=self.position+self.velocity
        


# In[9]:


#class to handle search space
class space():
    def __init__(self,target,target_error,n_particles):
        self.target=target
        self.target_error=target_error
        self.n_particles=n_particles
        self.particles=[]
        self.gbest_value=float('inf')
        self.gbest_position=np.array([random.random()*50,random.random()*50])
        
    def print_particles(self):
        for particle in self.particles :
            particle.__str__()
            
    def fitness(self,particles):
        return particles.position[0]**2 + particles.position[1]**2+1
    
    def set_pbest(self):
        for particle in self.particles:
            fitness_candidate=self.fitness(particle)
            if(particle.pbest_value > fitness_candidate):
                particle.pbest_value=fitness_candidate
                particle.pbest_position=particle.position
    
    def set_gbest(self):
        for particle in self.particles:
            best_fitness_candidate=self.fitness(particle)
            if(self.gbest_value > best_fitness_candidate):
                self.gbest_value=best_fitness_candidate
                self.gbest_position=particle.position
                
           
    def move_particles(self):
        for particle in self.particles :
            global W
            new_velocity = (W*particle.velocity) + (c1*random.random()) * (particle.pbest_position - particle.position) +                             (random.random()*c2) * (self.gbest_position - particle.position)
            particle.velocity=new_velocity
            particle.move()


# In[10]:


#main loop
search_space=space(1,target_error,n_particles)
particles_vector=[particle()for _ in range(search_space.n_particles)]
search_space.particles=particles_vector
search_space.print_particles()

iteration = 0
while(iteration < n_iterations):
    search_space.set_pbest()
    search_space.set_gbest()
    if(abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
        break
    search_space.move_particles()
    iteration+=1
print("the best solution is",search_space.gbest_position,"in n_iterations=",iteration)    

