import { Component, OnInit } from '@angular/core';
import { ModalService } from 'src/app/modal/modal.service';
import { ReportService } from './report.service';

@Component({
  selector: 'report-modal',
  templateUrl: 'report-modal.component.html',
  styleUrls: ['report-modal.component.scss'],
})
export class ReportModalComponent implements OnInit {
  constructor(
    private modalService: ModalService,
    private reportService: ReportService
  ) {}

  ngOnInit(): void {}

  close() {
    this.modalService.close();
  }
}
