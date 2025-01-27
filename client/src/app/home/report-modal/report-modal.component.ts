import { Component, Input, OnInit } from '@angular/core';
import { ModalService } from 'src/app/modal/modal.service';
import { ReportService } from './report.service';
import { ReportItem } from './report.model';

@Component({
  selector: 'report-modal',
  templateUrl: 'report-modal.component.html',
  styleUrls: ['report-modal.component.scss'],
})
export class ReportModalComponent implements OnInit {
  @Input()
  strict = false;

  reportItemList: ReportItem[] = [];

  constructor(
    private modalService: ModalService,
    private reportService: ReportService
  ) {}

  ngOnInit(): void {
    this.reportService
      .getCustomersReport$(this.strict)
      .subscribe((list) => (this.reportItemList = list));
  }

  close() {
    this.modalService.close();
  }
}
