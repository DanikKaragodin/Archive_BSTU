package lab4_1;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class lab4_1 extends JFrame implements ActionListener {
    private JButton redButton, yellowButton, greenButton;
    private JPanel trafficLightPanel, redLightPanel, yellowLightPanel, greenLightPanel, buttonPanel;
    private Color red, yellow, green; 
    private boolean redOn, yellowOn, greenOn; 
    public lab4_1() {
        setTitle("Traffic Light");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(200, 400);
        setLayout(new GridLayout(1, 2));

        trafficLightPanel = new JPanel();
        trafficLightPanel.setLayout(new GridLayout(0, 1,2,2));
        
        buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(0, 1,2,2));

        redButton = new JButton("Red");
        yellowButton = new JButton("Yellow");
        greenButton = new JButton("Green");
        
        buttonPanel.add(redButton);
        buttonPanel.add(yellowButton);
        buttonPanel.add(greenButton);
        
        red = new Color(127,0,0);
        yellow = new Color(127,127,0);
        green = new Color(0,127,0);
        
        redOn = false;
        yellowOn = false;
        greenOn = false; 
        
        redButton.addActionListener(this);
        yellowButton.addActionListener(this);
        greenButton.addActionListener(this);

        redLightPanel = new JPanel();
        redLightPanel.setBackground(red);
        yellowLightPanel = new JPanel();
        yellowLightPanel.setBackground(yellow);
        greenLightPanel = new JPanel();
        greenLightPanel.setBackground(green);

        trafficLightPanel.add(redLightPanel);
        trafficLightPanel.add(yellowLightPanel);
        trafficLightPanel.add(greenLightPanel);

        add(trafficLightPanel);
        add(buttonPanel);

        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == redButton) {
        	if(redOn) redLightPanel.setBackground(red);
        	else redLightPanel.setBackground(Color.RED);
        	redOn = !redOn;
        	return;
        }
        if (e.getSource() == yellowButton) {
        	if(yellowOn) yellowLightPanel.setBackground(yellow);
        	else yellowLightPanel.setBackground(Color.YELLOW);
        	yellowOn = !yellowOn;
        	return;
        }
        if (e.getSource() == greenButton) {
        	if(greenOn) greenLightPanel.setBackground(green);
        	else greenLightPanel.setBackground(Color.GREEN);
        	greenOn = !greenOn;
        	return;
        }
    }

    public static void main(String[] args) {
        new lab4_1();
    }
}