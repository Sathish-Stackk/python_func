import { useState } from "react";

function SkillTracker() {
  const [skills, setSkills] = useState([
    { name: "Python", level: 40 },
    { name: "React", level: 25 },
    { name: "SQL", level: 60 }
  ]);

  const improveSkill = (index) => {
    setSkills(skills.map((skill, i) =>
      i === index
        ? { ...skill, level: Math.min(skill.level + 10, 100) }
        : skill
    ));
  };

  return (
    <div>
      <h2>My Skill Progress</h2>

      {skills.map((skill, index) => (
        <div key={skill.name}>
          <p>{skill.name}: {skill.level}%</p>

          <progress value={skill.level} max="100" />

          <button onClick={() => improveSkill(index)}>
            Practice +10%
          </button>
        </div>
      ))}
    </div>
  );
}

export default SkillTracker;
