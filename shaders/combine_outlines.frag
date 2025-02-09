#version 330 core

out vec4 fragColor;

in vec2 uv;

uniform sampler2D baseOutline;
uniform sampler2D otherOutline;


void main()
{ 
    fragColor = texture(baseOutline, uv) - (1 - texture(otherOutline, uv));
    fragColor += 0.2;
}